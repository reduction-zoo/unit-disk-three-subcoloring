import itertools
import json
from pathlib import Path
import z3


def completions(n,edges,pins):
    c=[z3.Int(f'c{i}') for i in range(n)]
    s=z3.Solver()
    s.add(*[z3.And(v>=0,v<3) for v in c])
    s.add(*[c[a]!=c[b] for a,b in edges])
    s.add(*[c[i]==v for i,v in pins.items()])
    result=s.check()
    assert result in (z3.sat,z3.unsat)
    return [s.model().eval(v).as_long() for v in c] if result==z3.sat else None


clause_edges=[(0,3),(1,4),(2,5),(3,4),(3,6),(4,6),(6,7),(5,7),(5,8),(7,8)]
# Ports 0,1,2; internal y1..y6 are 3..8.
coords=[(x,y) for y in (-1,0,1) for x in (-1,0,1)]+[(0,3),(3,0),(0,-3),(-3,0)]
edges=[]
for i,(x,y) in enumerate(coords[:9]):
    for j,(u,v) in enumerate(coords[:i]):
        if abs(x-u)+abs(y-v)==1 and {i,j} not in ({6,3},{7,8},{5,2},{1,0}):
            edges.append((i,j))
for a,b in [(1,3),(3,7),(7,5),(5,1)]:
    edges.append((a,b))
for port,ids in [(9,[6,7,8]),(10,[2,5,8]),(11,[0,1,2]),(12,[0,3,6])]:
    edges.extend((port,i) for i in ids)

if __name__=='__main__':
    for colors in itertools.product(range(3),repeat=3):
        w=completions(9,clause_edges,dict(enumerate(colors))|{8:0})
        expected=colors!=(1,1,1) and colors!=(2,2,2)
        print(json.dumps({'event':'clause','inputs':colors,'expected':expected,'witness':w}),flush=True)
        assert (w is not None)==expected
    for colors in itertools.product(range(3),repeat=4):
        w=completions(13,edges,{i+9:c for i,c in enumerate(colors)})
        expected=colors[0]==colors[2] and colors[1]==colors[3]
        print(json.dumps({'event':'crossover','inputs':colors,'expected':expected,'witness':w}),flush=True)
        assert (w is not None)==expected
    Path(__file__).with_name('gadgets.json').write_text(json.dumps({'clause_edges':clause_edges,'cross_coords':coords,'cross_edges':edges}))
