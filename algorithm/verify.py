import argparse
import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[1]/'history/campaigns/unit-disk-three-subcoloring'


def source_decision(source):
    labels=sorted({abs(v) for clause in source['clauses'] for v in clause})
    return any(all(any(assignment[abs(v)]==(v>0) for v in clause) for clause in source['clauses']) for values in itertools.product((False,True),repeat=len(labels)) for assignment in [dict(zip(labels,values))])


def valid_recovery(source,witness):
    assert isinstance(witness,dict) and set(witness)=={'assignment'}
    assignment=witness['assignment'];assert isinstance(assignment,dict)
    assert all(k.isascii() and k.isdecimal() and k==str(int(k)) and 1<=int(k)<=source['n'] and type(v) is bool for k,v in assignment.items())
    assert all(any(assignment.get(str(abs(v)),False)==(v>0) for v in clause) for clause in source['clauses'])


def verify(candidate,evidence):
    output=Path(evidence) if evidence else Path(__file__).resolve().parents[1]/'evidence/additional-verification'
    output.mkdir(parents=True,exist_ok=False)
    spec=importlib.util.spec_from_file_location('projection',root/'rounds/052/project.py')
    p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
    spec=importlib.util.spec_from_file_location('target_search',root/'rounds/053/search.py')
    search=importlib.util.module_from_spec(spec);spec.loader.exec_module(search)
    graphs=p.bases();label=10**5000
    for name,clauses,baseline in [('sparse-positive',[[label,label,label]],'051'),('sparse-conflict',[[label,label,label],[-label,-label,-label]],'054')]:
        source={'n':label,'clauses':clauses};expected=source_decision(source)
        source_file=output/f'{name}-source.json';source_file.write_text(json.dumps(source))
        target_file=output/f'{name}-target.json'
        with target_file.open('w') as stream:
            subprocess.run([sys.executable,candidate],input=json.dumps(source),stdout=stream,text=True,check=True)
        points,scale=p.load_points(target_file)
        copies=json.loads((root/f'rounds/{baseline}/copies.json').read_text())
        terminals=p.project(points,scale,copies,graphs)
        witness=None if terminals is None else search.search(points,scale,copies,terminals,output/f'{name}-witness.json')
        if terminals is not None and witness is None:raise RuntimeError('target oracle returned unknown')
        assert (witness is not None)==expected
        recoveries=0
        if witness is not None:
            for permutation in itertools.permutations(range(3)):
                request={'source':source,'target_solution':[permutation[c] for c in witness]}
                recovered=json.loads(subprocess.run([sys.executable,candidate,'--extract'],input=json.dumps(request),capture_output=True,text=True,check=True).stdout)
                valid_recovery(source,recovered);recoveries+=1
        print(json.dumps({'case':name,'declaration_digits':5001,'active_variables':1,'vertices':len(points),'source':expected,'target':witness is not None,'recoveries':recoveries}),flush=True)
    malformed=[None,{}, {'n':True,'clauses':[]},{'n':-1,'clauses':[]},{'n':1,'clauses':[[0,1,1]]},{'n':1,'clauses':[[2,1,1]]}]
    for source in malformed:
        result=json.loads(subprocess.run([sys.executable,candidate],input=json.dumps(source),capture_output=True,text=True,check=True).stdout)
        assert result is None
    source={'n':label,'clauses':[]}
    result=json.loads(subprocess.run([sys.executable,candidate],input=json.dumps(source),capture_output=True,text=True,check=True).stdout)
    assert result=={'centers':[]}
    recovered=json.loads(subprocess.run([sys.executable,candidate,'--extract'],input=json.dumps({'source':source,'target_solution':[]}),capture_output=True,text=True,check=True).stdout)
    valid_recovery(source,recovered)
    print(json.dumps({'malformed_sources':6,'sparse_empty':True,'empty_recoveries':1}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--candidate',required=True);parser.add_argument('--evidence')
    args=parser.parse_args();verify(args.candidate,args.evidence)
