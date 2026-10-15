from fractions import Fraction
import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'013'))
import geometry
queries=0
for reverse in itertools.product((False,True),repeat=5):
    for middle in (-1,1):
        sides=[middle,-1,-1,-1,-1]
        flips=[-s if r else s for r,s in zip(reverse,sides)]
        t,adj,copies=geometry.compose([(0,0),(2,0),(1,Fraction(433,250)),(1,-Fraction(433,250))],
                                    [(0,1),(1,2),(2,0),(0,3),(3,1)],reverse,flips)
        w=geometry.lift(adj,copies,(0,1,2,2))
        canonical=w is not None and all(w[i]!=w[j] for i in range(4) for j in range(len(adj)) if adj[i][j])
        if not canonical:
            w=geometry.solve(adj,(0,1,2,2),True)
            queries+=1
        print(json.dumps({'reverse':reverse,'middle':middle,'status':'unsat' if w is None else 'sat',
                          'canonical_clean':canonical,'witness':w}),flush=True)
        if w is not None:
            Path(__file__).with_name('diamond.json').write_text(json.dumps(t))
            Path(__file__).with_name('witness.json').write_text(json.dumps(w))
            print(json.dumps({'event':'first_success','solver_queries':queries}),flush=True)
            sys.exit(0)
print(json.dumps({'event':'exhausted','solver_queries':queries}),flush=True)
