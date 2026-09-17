import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
root=Path(__file__).resolve().parents[2]
L=F(3969,1000)
min_nonedge=None;max_edge=F(0);max_l1=F(0)


def normalize(t):
    ps=wire.check.centers(t)
    out=[]
    for p in ps:
        x=L*sum(p[j]*wire.d[j] for j in range(2))/wire.dd
        y=L*(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd
        out.append([[v.numerator,v.denominator] for v in (x,y)])
    return {'centers':out}


def inspect(t,w,ports,name):
    global min_nonedge,max_edge,max_l1
    ps=wire.check.centers(t);a=wire.check.graph(t)
    assert wire.check.valid_coloring(a,w)
    assert all(w[i]!=w[j] for i in ports for j in range(len(ps)) if a[i][j])
    for i,j in itertools.combinations(range(len(ps)),2):
        dx,dy=ps[i][0]-ps[j][0],ps[i][1]-ps[j][1]
        sq=dx*dx+dy*dy
        max_l1=max(max_l1,abs(dx)+abs(dy))
        if a[i][j]:
            max_edge=max(max_edge,sq)
        else:
            min_nonedge=sq if min_nonedge is None else min(min_nonedge,sq)
    print(json.dumps({'event':'motif','name':name,'vertices':len(ps),'clean_valid':True}),flush=True)


for i,j in itertools.product(range(8),repeat=2):
    t,w,valid=wire.chain([wire.states[i],wire.states[j]])
    assert valid
    normalized=normalize(t)
    old=wire.check.graph(t);new=wire.check.graph(normalized)
    assert old==new
    inspect(normalized,w,range(3),f'wire-{i}-{j}')
for folder,name,graphfile,wfile,ports in [('020','junction','junction.json','witness.json',range(5)),
                                        ('021','arms-2','arms-2.json','witness-2.json',range(9)),
                                        ('021','arms-3','arms-3.json','witness-3.json',range(13))]:
    t=json.loads((root/f'rounds/{folder}/{graphfile}').read_text())
    w=json.loads((root/f'rounds/{folder}/{wfile}').read_text())
    normalized=normalize(t)
    assert wire.check.graph(t)==wire.check.graph(normalized)
    inspect(normalized,w,ports,name)
    Path(__file__).with_name(f'{name}.json').write_text(json.dumps(normalized))
t=json.loads((root/'rounds/022/connector.json').read_text())
w=json.loads((root/'rounds/022/witness.json').read_text())
inspect(t,w,range(6),'connector')
B=F(2025,394)*L*L/wire.dd
shrink=1-min((min_nonedge-1)/(4*min_nonedge),(B-4)/(4*B),F(1,100))
assert 0<shrink<1 and shrink*shrink*min_nonedge>1 and shrink*shrink*max_edge<1
assert shrink*shrink*B>4
margin=min(1-shrink*shrink*max_edge,shrink*shrink*min_nonedge-1)
epsilon=min(F(1),margin/(2*(4*max_l1+8)))
result={'min_nonedge_squared':str(min_nonedge),'max_edge_squared':str(max_edge),
        'max_l1_difference':str(max_l1),'shrink':str(shrink),'squared_margin':str(margin),
        'coordinate_perturbation':str(epsilon),'remote_arm_squared_bound':str(shrink*shrink*B)}
Path(__file__).with_name('margins.json').write_text(json.dumps(result))
print(json.dumps({'event':'margins',**result}),flush=True)
