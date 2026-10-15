import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
L=53*wire.F(749,10000)
for i,j in itertools.product((0,2,4,6),repeat=2):
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
    results=[];witnesses=[]
    for signal in (0,1):
        solver,c=wire.check.color_solver(a)
        for v in (33,34):solver.add(c[v]==0)
        for v in (68,69):solver.add(c[v]==signal)
        for v in (33,34,68,69):
            solver.add(*[c[v]!=c[u] for u in range(70) if a[v][u]])
        result=solver.check()
        assert result in (wire.z3.sat,wire.z3.unsat)
        w=[solver.model().eval(v).as_long() for v in c] if result==wire.z3.sat else None
        if w is not None:assert wire.check.valid_coloring(a,w)
        results.append(str(result));witnesses.append(w)
        print(json.dumps({'states':[i,j],'signal':signal,'status':str(result),'witness':w}),flush=True)
    if results==['sat','sat']:
        Path(__file__).with_name(f'crossing-{i}-{j}.json').write_text(json.dumps(t))
        Path(__file__).with_name(f'witnesses-{i}-{j}.json').write_text(json.dumps(witnesses))
