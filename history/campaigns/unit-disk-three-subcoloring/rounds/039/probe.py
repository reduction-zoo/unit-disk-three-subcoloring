import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from ortools.sat.python import cp_model
r=Path(__file__).parent
for name,path,ports_file,yes in [('yes',r/'yes-target.json',r/'yes-ports.json',True),('no',r.parent/'038/no-target.json',r.parent/'038/ports.json',False)]:
    t=json.loads(path.read_text());ps=[[Fraction(*v) for v in p] for p in t['centers']]
    scale=math.lcm(*(v.denominator for p in ps for v in p));ps=[tuple(int(v*scale) for v in p) for p in ps]
    adj=[set() for p in ps];buckets={}
    for i,(x,y) in enumerate(ps):
        cell=(x//scale,y//scale)
        for dx,dy in itertools.product((-1,0,1),repeat=2):
            for j in buckets.get((cell[0]+dx,cell[1]+dy),()):
                u,v=ps[j]
                if (x-u)**2+(y-v)**2<=scale**2:adj[i].add(j);adj[j].add(i)
        buckets.setdefault(cell,[]).append(i)
    m=cp_model.CpModel();c=[m.new_int_var(0,2,f'c{i}') for i in range(len(ps))];triples=0
    for b,ns in enumerate(adj):
        for a,d in itertools.combinations(sorted(ns),2):
            if d not in adj[a]:
                m.add_forbidden_assignments([c[a],c[b],c[d]],[(0,0,0),(1,1,1),(2,2,2)]);triples+=1
    print(json.dumps({'event':'encoded','case':name,'vertices':len(ps),'p3_constraints':triples}),flush=True)
    solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
    status=solver.solve(m);assert status in (cp_model.OPTIMAL,cp_model.INFEASIBLE)
    assert (status==cp_model.OPTIMAL)==yes
    recoveries=0
    if yes:
        w=[solver.value(v) for v in c]
        for b,ns in enumerate(adj):
            same=[a for a in ns if w[a]==w[b]]
            assert all(d in adj[a] for a,d in itertools.combinations(same,2))
        ports=json.loads(ports_file.read_text())
        for perm in itertools.permutations(range(3)):
            recovered=[perm[w[i]] for i in ports];assert len(set(recovered))==1;recoveries+=1
        (r/'solver-witness.json').write_text(json.dumps(w))
    print(json.dumps({'event':'solved','case':name,'status':solver.status_name(status),'network_recoveries':recoveries,'branches':solver.num_branches,'conflicts':solver.num_conflicts}),flush=True)
