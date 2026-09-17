import argparse
from fractions import Fraction
from itertools import combinations, product
import json
import re
from pathlib import Path
import subprocess
import sys
import z3
sys.set_int_max_str_digits(0)


def sat_result(solver):
    result=solver.check()
    if result==z3.unknown: raise RuntimeError(solver.reason_unknown())
    return result==z3.sat


def source_data(instance):
    n,clauses=instance['n'],instance['clauses']
    if type(n) is not int or n<0 or not isinstance(clauses,list): raise ValueError('Invalid formula')
    if any(not isinstance(c,list) or len(c)!=3 or any(type(x) is not int or not 1<=abs(x)<=n for x in c) for c in clauses):
        raise ValueError('Invalid 3SAT clause')
    return n,clauses


def source(instance):
    n,clauses=source_data(instance)
    variables={i:z3.Bool(f'x{i}') for i in {abs(l) for c in clauses for l in c}}
    solver=z3.Solver()
    solver.add(*[z3.Or(*[variables[abs(x)] if x>0 else z3.Not(variables[abs(x)]) for x in c]) for c in clauses])
    return sat_result(solver)


def source_witness(instance,witness):
    n,clauses=source_data(instance);values=witness['assignment']
    return (isinstance(values,dict)
            and all(isinstance(k,str) and k.isdecimal() and k==str(int(k)) and 1<=int(k)<=n and type(v) is bool for k,v in values.items())
            and all(any(values.get(str(abs(x)),False)==(x>0) for x in c) for c in clauses))


def graph(instance):
    n,edges=instance['n'],instance['edges']
    if type(n) is not int or n<0 or not isinstance(edges,list):raise ValueError('Invalid graph')
    if any(not isinstance(e,list) or len(e)!=2 or any(type(v) is not int for v in e) or not 0<=e[0]<e[1]<n for e in edges):
        raise ValueError('Invalid edge')
    if len(set(map(tuple,edges)))!=len(edges):raise ValueError('Repeated edge')
    return n,set(map(tuple,edges))


def target_witness(instance,witness,counts=None,depth=3):
    n,edges=graph(instance)
    if counts is None:counts=[2]*n
    if any(not isinstance(a,str) or re.fullmatch(r'-?[0-9]+(?:/[1-9][0-9]*)?',a) is None for row in witness['left'] for a in row):return False
    left=[[Fraction(a) for a in row] for row in witness['left']]
    if len(left)!=n or any(len(row)!=counts[i] for i,row in enumerate(left)):return False
    if any(any(abs(a-b)<1 for a,b in combinations(row,2)) for row in left):return False
    for u,v in combinations(range(n),2):
        if any(abs(a-b)<1 for a,b in product(left[u],left[v]))!=((u,v) in edges):return False
    starts=sum(left,[])
    return all(sum(b<=a<b+1 for b in starts)<=depth for a in starts)


def encoding(instance,counts=None,depth=3):
    n,edges=graph(instance)
    if counts is None:counts=[2]*n
    if len(counts)!=n or any(c not in (1,2) for c in counts):raise ValueError('Invalid slot counts')
    left=[[z3.Real(f'l{i}_{j}') for j in range(counts[i])] for i in range(n)]
    solver=z3.SolverFor('QF_LRA')
    if n:solver.add(left[0][0]==0)
    for row in left:
        if len(row)==2:solver.add(row[0]+1<=row[1])
    for u,v in combinations(range(n),2):
        overlap=z3.Or(*[z3.And(a<b+1,b<a+1) for a,b in product(left[u],left[v])])
        solver.add(overlap if (u,v) in edges else z3.Not(overlap))
    starts=sum(left,[])
    for a in starts:
        solver.add(z3.PbLe([(z3.And(b<=a,a<b+1),1) for b in starts],depth))
    return solver,left


def model_witness(solver,left):
    model=solver.model()
    return {'left':[[str(model.eval(a,model_completion=True).as_fraction()) for a in row] for row in left]}


def target(instance,counts=None,depth=3):
    if counts is None and depth==3:
        import split_oracle
        graph(instance)
        yes,witness,peeled=split_oracle.target(instance)
        if yes:assert target_witness(instance,witness)
        return yes,witness
    solver,left=encoding(instance,counts,depth)
    if not sat_result(solver):return False,None
    witness=model_witness(solver,left)
    assert target_witness(instance,witness,counts,depth)
    return True,witness


def call(candidate,payload,extract=False):
    output=subprocess.run([sys.executable,str(candidate)]+(['--extract'] if extract else []),input=json.dumps(payload),text=True,capture_output=True,check=True)
    return json.loads(output.stdout)


def test_candidate(candidate,cases):
    for case in cases:
        s=case['source'];g=call(candidate,s);yes,w=target(g)
        assert yes==source(s),case['name']
        recoveries=0
        if yes:
            for mirror in (False,True):
                y={'left':[[str(-Fraction(a)-1) if mirror else a for a in row] for row in w['left']]}
                assert target_witness(g,y)
                assert source_witness(s,call(candidate,{'source':s,'target_solution':y},True)),case['name']
                recoveries+=1
        print(json.dumps({'case':case['name'],'yes':yes,'recoveries':recoveries}),flush=True)


def self_test(cases):
    for c in cases:
        assert source(c['source'])==c['yes']
        _,clauses=source_data(c['source']);used=sorted({abs(l) for clause in clauses for l in clause})
        brute=any(source_witness(c['source'],{'assignment':dict(zip(map(str,used),a))}) for a in product((False,True),repeat=len(used)))
        assert brute==c['yes']
    targets=[({'n':0,'edges':[]},True),({'n':3,'edges':[[0,1],[0,2],[1,2]]},True),
             ({'n':5,'edges':[[0,i] for i in range(1,5)]},True),({'n':6,'edges':[[0,i] for i in range(1,6)]},False)]
    for g,expected in targets:assert target(g)[0]==expected
    assert target_witness({'n':2,'edges':[]},{'left':[['0','4'],['1','5']]})
    assert not target_witness({'n':2,'edges':[[0,1]]},{'left':[['0','4'],['1','5']]})
    assert not target_witness({'n':1,'edges':[]},{'left':[['0','1/2']]})
    assert not target_witness({'n':4,'edges':[list(e) for e in combinations(range(4),2)]},
                              {'left':[['0',str(10+2*i)] for i in range(4)]})
    try:graph({'n':2,'edges':[[0,1],[0,1]]})
    except ValueError:pass
    else:raise AssertionError('Repeated edge accepted')
    print(json.dumps({'source_cases':len(cases),'independent_boolean_enumerations':len(cases),'target_decisions':4,'witness_regressions':4,'malformed_graphs':1,'z3':z3.get_version_string()}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test',action='store_true');group.add_argument('--candidate',type=Path)
    args=parser.parse_args();cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    if args.self_test:self_test(cases)
    else:test_candidate(args.candidate,cases)
