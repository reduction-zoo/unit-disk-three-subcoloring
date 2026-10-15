import itertools
import json
from pathlib import Path
import z3
root=Path(__file__).resolve().parents[2]
r=Path(__file__).parent
network=json.loads((root/'rounds/031/network.json').read_text())
paths=json.loads((root/'rounds/031/paths.json').read_text())
axes=[sorted({p[k] for e in paths for p in e['points']}) for k in range(2)]
for e in paths:
    points=[]
    for p in e['points']:
        q=tuple(axes[k].index(p[k]) for k in range(2))
        while len(points)>1 and ((points[-2][0]==points[-1][0]==q[0]) or (points[-2][1]==points[-1][1]==q[1])):
            points.pop()
        points.append(q)
    e['points']=points
    e['kind']=next(k for a,b,k in network['edges'] if set((a,b))==set(e['ends']))
segments=[(i,a,b) for i,e in enumerate(paths) for a,b in zip(e['points'],e['points'][1:])]
centers={v:p for e in paths for v,p in zip(e['ends'],(e['points'][0],e['points'][-1]))}
for (i,a,b),(j,c,d) in itertools.combinations(segments,2):
    assert a[0]==b[0] or a[1]==b[1]
    if i==j:continue
    lo=[max(min(a[k],b[k]),min(c[k],d[k])) for k in range(2)]
    hi=[min(max(a[k],b[k]),max(c[k],d[k])) for k in range(2)]
    if any(lo[k]>hi[k] for k in range(2)):continue
    common=set(paths[i]['ends'])&set(paths[j]['ends'])
    assert lo==hi and tuple(lo) in [centers[v] for v in common]
for colors in itertools.product(range(3),repeat=4):
    c=[z3.Int(f'c{i}') for i in network['points']]
    s=z3.Solver();s.add(*[z3.And(v>=0,v<3) for v in c])
    for a,b,k in network['edges']:s.add(c[a]==c[b] if k=='eq' else c[a]!=c[b])
    s.add(*[c[v]==color for v,color in zip(network['ports'],colors)])
    status=s.check();assert status in (z3.sat,z3.unsat)
    assert (status==z3.sat)==(colors[0]==colors[2] and colors[1]==colors[3])
    w=[s.model().eval(v).as_long() for v in c] if status==z3.sat else None
    print(json.dumps({'ports':colors,'status':str(status),'witness':w}),flush=True)
(r/'routing.json').write_text(json.dumps({'vertices':{str(v):p for v,p in centers.items()},'paths':paths,'ports':network['ports']}))
print(json.dumps({'event':'size','vertices':len(centers),'paths':len(paths),'segments':len(segments),'unit_length':sum(abs(a[0]-b[0])+abs(a[1]-b[1]) for i,a,b in segments),'box':[len(a)-1 for a in axes],'ports':[centers[v] for v in network['ports']]}),flush=True)
