import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import numpy as np
from ortools.sat.python import cp_model
r=Path(__file__).parent
root=r.parents[1]


def load_points(path):
    t=json.loads(Path(path).read_text())
    assert isinstance(t,dict) and set(t)=={'centers'}
    ps=t['centers']
    assert isinstance(ps,list)
    assert all(isinstance(p,list) and len(p)==2 and all(isinstance(v,list) and len(v)==2 and all(type(x) is int for x in v) and v[1]>0 for v in p) for p in ps)
    scale=math.lcm(*(v[1] for p in ps for v in p))
    assert 2*scale*scale<2**63
    values=[[a*(scale//b) for a,b in p] for p in ps]
    assert all(abs(v)<2**51 for pair in values for v in pair)
    points=np.array(values,dtype=np.int64).reshape(-1,2)
    return points,scale


def induced(points,scale,ids):
    assert len(ids)==35 and len(set(ids))==35 and all(type(i) is int and 0<=i<len(points) for i in ids)
    ps=points[ids]
    delta=ps[:,None,:]-ps[None,:,:]
    assert np.max(np.abs(delta))<2**30
    adj=np.sum(delta*delta,axis=2)<=scale*scale
    np.fill_diagonal(adj,False)
    return adj


def bases():
    result={}
    for kind,path in [('eq','rounds/017/equality.json'),('ne','rounds/012/gadget.json')]:
        ps,scale=load_points(root/path);a=induced(ps,scale,list(range(35)))
        m=cp_model.CpModel();c=[m.new_int_var(0,2,f'c{i}') for i in range(35)]
        for ids in itertools.combinations(range(35),3):
            if sum(bool(a[i,j]) for i,j in itertools.combinations(ids,2))==2:
                m.add_forbidden_assignments([c[i] for i in ids],[(0,0,0),(1,1,1),(2,2,2)])
        m.add(c[-2]==0);m.add(c[-1]==(1 if kind=='eq' else 0))
        solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
        status=solver.solve(m);assert status==cp_model.INFEASIBLE
        result[kind]=a
        print(json.dumps({'event':'forbidden_relation','kind':kind,'status':solver.status_name(status)}),flush=True)
    return result


def project(points,scale,copies,graphs):
    parent={}
    def find(a):
        parent.setdefault(a,a)
        while parent[a]!=a:
            parent[a]=parent[parent[a]];a=parent[a]
        return a
    for kind,ids in copies:
        assert kind in graphs and np.array_equal(induced(points,scale,ids),graphs[kind])
        a,b=map(find,ids[-2:])
        if kind=='eq':parent[a]=b
    representatives={i:find(i) for i in list(parent)}
    m=cp_model.CpModel();colors={i:m.new_int_var(0,2,f'p{i}') for i in sorted(set(representatives.values()))}
    for kind,ids in copies:
        if kind=='ne':m.add(colors[representatives[ids[-2]]]!=colors[representatives[ids[-1]]])
    solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
    status=solver.solve(m);assert status in (cp_model.OPTIMAL,cp_model.INFEASIBLE)
    values={i:solver.value(colors[v]) for i,v in representatives.items()} if status==cp_model.OPTIMAL else None
    print(json.dumps({'event':'projection','copies_checked':len(copies),'terminal_classes':len(colors),'status':solver.status_name(status),'target_decision':'NO' if values is None else 'unknown'}),flush=True)
    return values


if __name__=='__main__':
    graphs=bases();points,scale=load_points(r.parent/'051/target.json')
    copies=json.loads((r.parent/'051/copies.json').read_text())
    values=project(points,scale,copies,graphs)
    assert values is not None
    (r/'terminal-colors.json').write_text(json.dumps(values))
    bad=list(copies[0][1]);bad[0]=len(points)-1
    try:
        assert np.array_equal(induced(points,scale,bad),graphs[copies[0][0]])
    except AssertionError:
        print(json.dumps({'event':'corrupt_manifest','rejected':True}),flush=True)
    else:raise AssertionError('corrupt manifest accepted')
