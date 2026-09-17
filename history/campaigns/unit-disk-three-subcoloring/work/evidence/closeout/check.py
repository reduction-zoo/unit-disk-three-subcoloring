import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
import z3
root=Path(__file__).resolve().parents[3]


def adjacency(t):
    den=math.lcm(*(v[1] for p in t['centers'] for v in p))
    ps=[tuple(v[0]*(den//v[1]) for v in p) for p in t['centers']]
    return [[i!=j and (p[0]-q[0])**2+(p[1]-q[1])**2<=den**2
             for j,q in enumerate(ps)] for i,p in enumerate(ps)]


def validate(a,w,terminals):
    assert len(a)==len(w) and all(type(c) is int and c in (0,1,2) for c in w)
    for triple in itertools.combinations(range(len(a)),3):
        if len({w[i] for i in triple})==1:
            assert sum(a[i][j] for i,j in itertools.combinations(triple,2))!=2
    assert all(w[i]!=w[j] for i in terminals for j in range(len(a)) if a[i][j])


rows=[json.loads(s) for s in (root/'rounds/012/output.jsonl').read_text().splitlines()]
i_graph=json.loads((root/'rounds/012/gadget.json').read_text())
i_witness=next(r['clean'] for r in rows if r['event']=='joint' and r['ports']==i_graph['centers'][-2:])
items=[('inequality',i_graph,i_witness,[33,34])]
for name,folder,graphfile,terminals in [('triangle','014','triangle.json',[0,1,2]),
                                      ('equality','017','equality.json',[33,34]),
                                      ('wire','018','three-copy.json',[0,1,2,3]),
                                      ('junction','020','junction.json',[0,1,2,3,4])]:
    items.append((name,json.loads((root/f'rounds/{folder}/{graphfile}').read_text()),
                  json.loads((root/f'rounds/{folder}/witness.json').read_text()),terminals))
for name,t,w,terminals in items:
    a=adjacency(t)
    validate(a,w,terminals)
    print(json.dumps({'artifact':name,'vertices':len(a),'clean_witness_valid':True}),flush=True)
    if name not in ('inequality','equality'):
        continue
    colors=[[z3.Bool(f'{name}_{i}_{c}') for c in range(3)] for i in range(len(a))]
    q=z3.Solver()
    for cs in colors:
        q.add(z3.PbEq([(c,1) for c in cs],1))
    for center in range(len(a)):
        ns=[v for v in range(len(a)) if a[center][v]]
        for left,right in itertools.combinations(ns,2):
            if not a[left][right]:
                for c in range(3):
                    q.add(z3.Or(z3.Not(colors[left][c]),z3.Not(colors[center][c]),z3.Not(colors[right][c])))
    q.add(colors[33][0],colors[34][0 if name=='inequality' else 1])
    status=q.check()
    assert status==z3.unsat,str(status)
    print(json.dumps({'artifact':name,'independent_boolean_forbidden_relation':str(status),'solver':z3.get_version_string()}),flush=True)
