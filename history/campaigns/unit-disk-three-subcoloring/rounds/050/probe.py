import importlib.util
import itertools
import json
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('g',r.parent/'048/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
assert (334-180)*g.q>2
for units,direction,ca,cb in itertools.product((1,2),((1,0),(0,1),(-1,0),(0,-1)),range(3),range(3)):
    d=g.Drawing();a=(0,0);b=tuple(units*g.step*v for v in direction)
    d.hub(a,ca);d.hub(b,cb);d.segment(a,b,ca!=cb,ca,cb)
    dx,dy=direction;length=units*g.step*g.q
    distances=[]
    for x,y in d.points:
        along=x*dx+y*dy;lateral=-x*dy+y*dx
        excess=max(0,-along,along-length)
        distances.append(excess**2+lateral**2)
    bound=max(distances);assert bound<=(90*g.q)**2
    print(json.dumps({'units':units,'direction':direction,'colors':[ca,cb],'max_squared_distance':str(bound),'support':True}),flush=True)
