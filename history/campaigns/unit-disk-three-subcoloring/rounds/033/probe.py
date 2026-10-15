import itertools
import json
from pathlib import Path
import geometry as g
r=Path(__file__).parent
for name in ('rounds/012/gadget.json','rounds/014/triangle.json','rounds/017/equality.json','rounds/018/three-copy.json','rounds/020/junction.json'):
    t=json.loads((g.root/name).read_text());ps=g.wire.check.centers(t)
    sparse=g.adjacency(ps);dense=g.wire.check.graph(t)
    assert all(sparse[i]=={j for j,x in enumerate(row) if x} for i,row in enumerate(dense))
    print(json.dumps({'event':'checker_comparison','file':name,'vertices':len(ps)}),flush=True)
for direction in ((1,0),(0,1),(-1,0),(0,-1)):
    for ca,cb in itertools.product(range(3),repeat=2):
        d=g.Drawing();a=(0,0);b=tuple(g.step*v for v in direction)
        d.hub(a,ca);d.hub(b,cb);d.segment(a,b,ca!=cb,ca,cb)
        valid,failure,adj=g.validate(d.points,d.colors)
        print(json.dumps({'direction':direction,'colors':[ca,cb],'vertices':len(d.points),'valid':valid,'failure':failure}),flush=True)
        if not valid:
            (r/'failure.json').write_text(json.dumps({'target':d.target(),'witness':d.colors,'p3':failure}))
            raise AssertionError('invalid composed coloring')
        for kind,ids in d.copies:
            original=g.wire.original if kind=='eq' else g.wire.check.graph(g.I)
            assert [[v in adj[u] for v in ids] for u in ids]==original
        if direction==(1,0) and ca==0 and cb==1:
            (r/'edge.json').write_text(json.dumps(d.target()));(r/'witness.json').write_text(json.dumps(d.colors))
