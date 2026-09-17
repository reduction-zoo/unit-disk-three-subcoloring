import json
import random
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
for n in (24,36,48,60):
    for side in (2,3,4):
        for seed in range(8):
            rng=random.Random(10000*n+100*side+seed)
            ps=set()
            while len(ps)<n:
                ps.add((rng.randrange(100*side+1),rng.randrange(100*side+1)))
            t={'centers':[[[x,100],[y,100]] for x,y in sorted(ps)]}
            ident={'n':n,'side':side,'seed':seed}
            print(json.dumps({'event':'start',**ident}),flush=True)
            w=check.solve_coloring(check.graph(t))
            print(json.dumps({'event':'result',**ident,'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
            if w is None:
                Path(__file__).with_name('obstruction.json').write_text(json.dumps(t))
                sys.exit(0)
