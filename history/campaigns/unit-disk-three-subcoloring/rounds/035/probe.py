import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from ortools.sat.python import cp_model
root=Path(__file__).resolve().parents[2]
for name,expected_equal in [('rounds/012/gadget.json',False),('rounds/017/equality.json',True)]:
    t=json.loads((root/name).read_text());points=[[Fraction(*v) for v in p] for p in t['centers']]
    scale=math.lcm(*(v.denominator for p in points for v in p));ps=[[int(v*scale) for v in p] for p in points];n=len(ps)
    a=[[i!=j and sum((ps[i][k]-ps[j][k])**2 for k in range(2))<=scale**2 for j in range(n)] for i in range(n)]
    triples=[ids for ids in itertools.combinations(range(n),3) if sum(a[i][j] for i,j in itertools.combinations(ids,2))==2]
    for equal,clean in [(True,False),(False,False),(expected_equal,True)]:
        m=cp_model.CpModel();c=[m.new_int_var(0,2,f'c{i}') for i in range(n)]
        for ids in triples:m.add_forbidden_assignments([c[i] for i in ids],[(0,0,0),(1,1,1),(2,2,2)])
        m.add(c[-2]==0);m.add(c[-1]==(0 if equal else 1))
        if clean:
            for i in (n-2,n-1):
                for j in range(n):
                    if a[i][j]:m.add(c[i]!=c[j])
        s=cp_model.CpSolver();status=s.solve(m)
        assert status in (cp_model.OPTIMAL,cp_model.FEASIBLE,cp_model.INFEASIBLE)
        feasible=status!=cp_model.INFEASIBLE
        assert feasible==(equal==expected_equal)
        w=[s.value(v) for v in c] if feasible else None
        if w is not None:assert all(len({w[i] for i in ids})>1 for ids in triples)
        print(json.dumps({'file':name,'equal':equal,'clean':clean,'status':s.status_name(status),'witness':w,'branches':s.num_branches,'conflicts':s.num_conflicts}),flush=True)
