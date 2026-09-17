import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'work'))
import check
for size in (4,5,6):
    for num, den in ((1,2),(2,5),(1,3),(3,5)):
        t = {'centers': [[[i*num,den],[j*num,den]] for i in range(size) for j in range(size)]}
        print(json.dumps({'event':'start','size':size,'spacing':[num,den]}),flush=True)
        w = check.solve_coloring(check.graph(t))
        print(json.dumps({'event':'result','size':size,'spacing':[num,den],
                          'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
