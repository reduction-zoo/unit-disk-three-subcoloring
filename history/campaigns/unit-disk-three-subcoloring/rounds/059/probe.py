import itertools
import json
from fractions import Fraction
from pathlib import Path
import z3
from ortools.sat.python import cp_model
r=Path(__file__).parent
root=r.parents[1]
for kind,path in [('eq','rounds/017/equality.json'),('ne','rounds/012/gadget.json')]:
    points=[[Fraction(*v) for v in p] for p in json.loads((root/path).read_text())['centers']]
    adjacent=lambda a,b:sum((x-y)**2 for x,y in zip(points[a],points[b]))<=1
    triples=[ids for ids in itertools.combinations(range(35),3) if sum(adjacent(a,b) for a,b in itertools.combinations(ids,2))==2]
    colors=[z3.Int(f'c{i}') for i in range(35)]
    domain=[z3.And(c>=0,c<3) for c in colors]+[colors[-2]==0,colors[-1]==(1 if kind=='eq' else 0)]
    constraints=[z3.Or(colors[a]!=colors[b],colors[b]!=colors[c]) for a,b,c in triples]
    q=z3.Solver();q.add(*domain)
    for i,formula in enumerate(constraints):q.assert_and_track(formula,z3.Bool(f't{i}'))
    assert q.check()==z3.unsat
    indices=sorted(int(str(x)[1:]) for x in q.unsat_core());initial=len(indices);checks=0
    for removed in list(indices)[:100]:
        trial=[i for i in indices if i!=removed]
        solver=z3.Solver();solver.add(*domain,*[constraints[i] for i in trial])
        status=solver.check();assert status in (z3.sat,z3.unsat);checks+=1
        if status==z3.unsat:indices=trial
    kernel=[triples[i] for i in indices]
    m=cp_model.CpModel();c=[m.new_int_var(0,2,f'c{i}') for i in range(35)]
    m.add(c[-2]==0);m.add(c[-1]==(1 if kind=='eq' else 0))
    for ids in kernel:
        assert sum(adjacent(a,b) for a,b in itertools.combinations(ids,2))==2
        m.add_forbidden_assignments([c[i] for i in ids],[(0,0,0),(1,1,1),(2,2,2)])
    solver=cp_model.CpSolver();solver.parameters.num_search_workers=1
    status=solver.solve(m);assert status==cp_model.INFEASIBLE
    (r/f'{kind}-kernel.json').write_text(json.dumps({'vertices':35,'terminal_colors':[0,1 if kind=='eq' else 0],'p3_constraints':kernel}))
    print(json.dumps({'kind':kind,'all_p3':len(triples),'initial_core':initial,'retained_core':len(kernel),'z3_queries':1+checks,'cp_sat_queries':1,'status':solver.status_name(status),'minimality_claimed':False}),flush=True)
