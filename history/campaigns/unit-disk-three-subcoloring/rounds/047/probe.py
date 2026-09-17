import importlib.util
import itertools
import json
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('g',r.parent/'044/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
h=(F(1),F(0));up=(F(4,5),F(3,5));down=(F(4,5),F(-3,5))
for directions,states in itertools.product(((h,up),(up,h),(h,down),(down,h)),itertools.product((0,1,4,5),repeat=2)):
    d=g.Drawing();p=(F(0),F(0))
    for direction,state in zip(directions,states):p=d.equality(p,direction,50,state,0)
    valid,failure,adj=g.validate(d.points,d.colors)
    local=all([[v in adj[u] for v in ids] for u in ids]==g.wire.original for kind,ids in d.copies)
    clean=valid and all(d.colors[i]!=d.colors[j] for i in d.terminals.values() for j in adj[i])
    print(json.dumps({'directions':[[str(v) for v in p] for p in directions],'states':states,'induced':local,'clean':clean,'failure':failure}),flush=True)
