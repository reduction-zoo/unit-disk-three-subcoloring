from fractions import Fraction
import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'013'))
import geometry
import z3
queries=0
for reverse in itertools.product((False,True),repeat=5):
    for middle in (-1,1):
        sides=[middle,-1,-1,-1,-1]
        flips=[-s if r else s for r,s in zip(reverse,sides)]
        t,adj,copies=geometry.compose([(0,0),(2,0),(1,Fraction(433,250)),(1,-Fraction(433,250))],
                                    [(0,1),(1,2),(2,0),(0,3),(3,1)],reverse,flips)
        w=geometry.solve(adj,(0,1,2,2),False)
        queries+=1
        print(json.dumps({'reverse':reverse,'middle':middle,'clean':False,'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
        if w is None:
            continue
        q,vs=geometry.check.color_solver(adj)
        q.add([vs[i]==c for i,c in enumerate((0,1,2,2))])
        q.add([vs[i]!=vs[j] for i in (2,3) for j in range(len(adj)) if adj[i][j]])
        status=q.check();queries+=1
        out={'reverse':reverse,'middle':middle,'clean':True,'status':str(status)}
        if status==z3.sat:
            w=[q.model().eval(v).as_long() for v in vs]
            assert geometry.check.valid_coloring(adj,w)
            assert all(w[i]!=w[j] for i in (2,3) for j in range(len(adj)) if adj[i][j])
            out['witness']=w
            Path(__file__).with_name('diamond.json').write_text(json.dumps(t))
            Path(__file__).with_name('witness.json').write_text(json.dumps(w))
            print(json.dumps(out),flush=True)
            print(json.dumps({'event':'first_success','solver_queries':queries}),flush=True)
            sys.exit(0)
        if status!=z3.unsat:
            raise RuntimeError(str(status))
        print(json.dumps(out),flush=True)
print(json.dumps({'event':'exhausted','solver_queries':queries}),flush=True)
