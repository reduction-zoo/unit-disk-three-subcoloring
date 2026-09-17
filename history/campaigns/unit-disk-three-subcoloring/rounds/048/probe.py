import itertools
import json
from pathlib import Path
import geometry as g
r=Path(__file__).parent
for units,direction,ca,cb in itertools.product((1,2),((1,0),(0,1),(-1,0),(0,-1)),range(3),range(3)):
    d=g.Drawing();a=(0,0);b=tuple(units*g.step*v for v in direction)
    d.hub(a,ca);d.hub(b,cb);d.segment(a,b,ca!=cb,ca,cb)
    valid,failure,adj=g.validate(d.points,d.colors)
    local=all([[v in adj[u] for v in ids] for u in ids]==(g.wire.original if kind=='eq' else g.wire.check.graph(g.I)) for kind,ids in d.copies)
    print(json.dumps({'units':units,'direction':direction,'colors':[ca,cb],'vertices':len(d.points),'valid':valid,'induced':local,'failure':failure}),flush=True)
    if not valid or not local:
        (r/'failure.json').write_text(json.dumps({'target':d.target(),'witness':d.colors,'p3':failure}))
        raise AssertionError('short segment failed')
