import importlib.util
import itertools
import json
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('g',r.parent/'048/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
for colors in itertools.product(range(3),repeat=4):
    d=g.Drawing();d.hub((0,0),0)
    for direction,color in zip(((1,0),(0,1),(-1,0),(0,-1)),colors):
        b=tuple(2*g.step*v for v in direction);d.hub(b,color);d.segment((0,0),b,color!=0,0,color)
    valid,failure,adj=g.validate(d.points,d.colors)
    local=all([[v in adj[u] for v in ids] for u in ids]==(g.wire.original if kind=='eq' else g.wire.check.graph(g.I)) for kind,ids in d.copies)
    print(json.dumps({'outer_colors':colors,'vertices':len(d.points),'valid':valid,'induced':local,'failure':failure}),flush=True)
    if not valid or not local:
        (r/'failure.json').write_text(json.dumps({'target':d.target(),'witness':d.colors,'p3':failure}))
        raise AssertionError('branching failed')
