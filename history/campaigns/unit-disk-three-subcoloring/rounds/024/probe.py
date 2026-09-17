import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
root=Path(__file__).resolve().parents[2]
q=wire.F(749,10000)


def pair(i,j,first,second):
    lengths=[first,second]
    points=[[wire.F(0),wire.F(0)],[first,wire.F(0)],[first+second,wire.F(0)]]
    w=[0,0,0];copies=[]
    for cell,state_id in enumerate((i,j)):
        state=wire.states[state_id]
        ps,cs=wire.single(state);ids=[]
        for p,c in zip(ps,cs):
            u=sum(p[k]*wire.d[k] for k in range(2))/wire.dd
            v=(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd
            ids.append(len(points))
            points.append([(0 if cell==0 else first)+lengths[cell]*u,lengths[cell]*v]);w.append(c)
        ports=[cell,cell+1]
        if state[0]:
            ports.reverse()
        copies.append(ids+ports)
    t={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    a=wire.check.graph(t)
    local=all([[a[i][j] for j in ids] for i in ids]==wire.original for ids in copies)
    valid=local and wire.check.valid_coloring(a,w)
    clean=valid and all(w[i]!=w[j] for i in range(3) for j in range(len(a)) if a[i][j])
    return local,clean


for x,y in itertools.product((52,53),repeat=2):
    for i,j in itertools.product(range(8),repeat=2):
        local,clean=pair(i,j,x*q,y*q)
        print(json.dumps({'event':'pair','length_units':[x,y],'states':[i,j],'local':local,'clean_valid':clean}),flush=True)
t=json.loads((root/'rounds/020/junction.json').read_text())
w=json.loads((root/'rounds/020/witness.json').read_text())
points=[]
for p in wire.check.centers(t):
    x=52*q*sum(p[k]*wire.d[k] for k in range(2))/wire.dd
    y=52*q*(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd
    points.append([[v.numerator,v.denominator] for v in (x,y)])
new={'centers':points};a=wire.check.graph(new)
local=wire.check.graph(t)==a
clean=wire.check.valid_coloring(a,w) and all(w[i]!=w[j] for i in range(5) for j in range(len(a)) if a[i][j])
print(json.dumps({'event':'junction','same_adjacency':local,'clean_valid':clean}),flush=True)
if local and clean:
    Path(__file__).with_name('junction.json').write_text(json.dumps(new))
