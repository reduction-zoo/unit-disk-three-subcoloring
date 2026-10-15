import importlib.util
import itertools
import json
from collections import Counter
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('g',r.parent/'048/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
def strip(d,direction,boundary,color):
    dx,dy=direction;items=[]
    for (x,y),c in zip(d.points,d.colors):
        along=x*dx+y*dy-boundary;lateral=-x*dy+y*dx
        if abs(along)<=2:items.append((along,lateral,(c-color)%3))
    return Counter(items)
base=g.Drawing();base.hub((0,0),0);base.hub((2*g.step,0),0);base.segment((0,0),(2*g.step,0),False,0,0)
reference=strip(base,(1,0),g.step*g.q,0)
for units,direction,ca,cb in itertools.product((3,4,5),((1,0),(0,1),(-1,0),(0,-1)),range(3),range(3)):
    d=g.Drawing();b=tuple(units*g.step*v for v in direction)
    d.hub((0,0),ca);d.hub(b,cb);d.segment((0,0),b,ca!=cb,ca,cb)
    valid,failure,adj=g.validate(d.points,d.colors)
    assert valid,failure
    assert all([[v in adj[u] for v in ids] for u in ids]==(g.wire.original if kind=='eq' else g.wire.check.graph(g.I)) for kind,ids in d.copies)
    for boundary in range(1,units):assert strip(d,direction,boundary*g.step*g.q,cb)==reference
    print(json.dumps({'units':units,'direction':direction,'colors':[ca,cb],'valid':True,'boundary_comparisons':units-1}),flush=True)
