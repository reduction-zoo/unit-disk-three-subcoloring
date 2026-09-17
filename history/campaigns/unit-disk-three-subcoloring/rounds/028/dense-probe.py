import itertools
import json
import sys
from pathlib import Path
import source
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3

clauses=list(itertools.product((1,-1),repeat=3))
cases=[{'n':1,'clauses':list(cs)} for k in range(3) for cs in itertools.combinations_with_replacement(clauses,k)]
cases += [{'n':2,'clauses':[c]} for c in itertools.product((1,-1,2,-2),repeat=3)]
cases += [{'n':0,'clauses':[]},{'n':3,'clauses':list(itertools.product((1,-1),(2,-2),(3,-3)))},{'n':3,'clauses':list(itertools.product((1,-1),(2,-2),(3,-3)))[:-1]}]
for index,s in enumerate(cases):
    s['clauses']=[list(c) for c in s['clauses']]
    n,edges=source.construct(s)
    c=[z3.Int(f'c{i}') for i in range(n)]
    solver=z3.Solver();solver.add(*[z3.And(v>=0,v<3) for v in c]);solver.add(*[c[a]!=c[b] for a,b in edges])
    result=solver.check();assert result in (z3.sat,z3.unsat)
    yes=check.source_solve(s) is not None
    assert (result==z3.sat)==yes
    recoveries=0
    if yes:
        w=[solver.model().eval(v).as_long() for v in c]
        for perm in itertools.permutations(range(3)):
            assert check.source_witness(s,source.extract(s,[perm[x] for x in w]))
            recoveries+=1
    print(json.dumps({'case':index,'source':s,'vertices':n,'yes':yes,'recoveries':recoveries}),flush=True)
