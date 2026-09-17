import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
L=53*wire.F(749,10000)
for i,j in itertools.product(range(8),repeat=2):
    points=[];base=[];copies=[]
    for axis,state_id in enumerate((i,j)):
        state=wire.states[state_id];ps,cs=wire.single(state)
        ps=ps+[[wire.F(0),wire.F(0)],wire.d];cs=cs+[0,0]
        for p in ps:
            x=L*(sum(p[k]*wire.d[k] for k in range(2))/wire.dd-wire.F(1,2))
            y=L*(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd
            points.append([x,y] if axis==0 else [-y,x])
        base.extend(cs)
        ids=list(range(axis*35,(axis+1)*35))
        if state[0]:ids[-2:]=ids[-2:][::-1]
        copies.append(ids)
    t={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    a=wire.check.graph(t)
    assert all([[a[u][v] for v in ids] for u in ids]==wire.original for ids in copies)
    results=[]
    for signal in (0,1):
        w=base[:35]+[(c+signal)%3 for c in base[35:]]
        results.append(wire.check.valid_coloring(a,w))
    print(json.dumps({'states':[i,j],'same_different_valid':results}),flush=True)
    if all(results):
        Path(__file__).with_name(f'crossing-{i}-{j}.json').write_text(json.dumps(t))
