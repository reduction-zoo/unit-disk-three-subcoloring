import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
for size,num,den in ((7,2,5),(8,1,3),(9,1,2)):
    t={'centers':[[[i*num,den],[j*num,den]] for i in range(size) for j in range(size)]}
    print(json.dumps({'event':'start','side':size,'spacing':[num,den]}),flush=True)
    w=check.solve_coloring(check.graph(t))
    print(json.dumps({'event':'result','side':size,'spacing':[num,den],'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
    if w is None:
        Path(__file__).with_name('obstruction.json').write_text(json.dumps(t))
        break
