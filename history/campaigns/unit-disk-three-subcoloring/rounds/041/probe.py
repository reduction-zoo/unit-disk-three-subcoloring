import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('geom',r.parent/'038/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
for kind,ps,grid,base in [('eq',g.E+[(F(0),F(0)),(F(1),F(0))],range(50,61),52*g.q),('ne',[(x/27,y/27) for x,y in g.I]+[(F(0),F(0)),(F(1),F(0))],range(25,31),27*g.q)]:
    distances=[sum((a-b)**2 for a,b in zip(p,q)) for i,p in enumerate(ps) for q in ps[i+1:]]
    expected=[d*base**2<=1 for d in distances]
    low=max(1/d for d,edge in zip(distances,expected) if not edge)
    high=min(1/d for d,edge in zip(distances,expected) if edge and d)
    print(json.dumps({'kind':kind,'squared_span_interval_open_left':[str(low),str(high)],'tests':[{'units':k,'same_graph':[d*(k*g.q)**2<=1 for d in distances]==expected} for k in grid]}))
