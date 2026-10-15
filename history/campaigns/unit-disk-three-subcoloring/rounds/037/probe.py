import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'033'))
import geometry as g
L=52*g.q;U=53*g.q
M=max(abs(y) for ps,cs in g.E for x,y in ps)
assert all(0<=x<=1 for ps,cs in g.E for x,y in ps)
arm_gap=L-M*U
ip=[((p[0]-g.ip[-2][0])*27*g.q/2,(p[1]-g.ip[-2][1])*27*g.q/2) for p in g.ip]
imin=min(x for x,y in ip);imax=max(x for x,y in ip)
radius=max(U,max(abs(v) for p in ip for v in p))
assert arm_gap>2 and L>2 and 27*g.q>2
assert L+imin>2 and L+27*g.q-imax>2
assert g.step*g.q-2*radius>2
print(json.dumps({'event':'bounds','q':str(g.q),'lateral_ratio':str(M),'orthogonal_remote_gap':str(arm_gap),'I_projection':[str(imin),str(imax)],'feature_radius':str(radius),'unrelated_gap':str(g.step*g.q-2*radius)}),flush=True)
for file in sorted((g.root/'rounds/036').glob('*-network.json')):
    net=json.loads(file.read_text());ps=net['points'];segments=net['segments'];degree=[0]*len(ps)
    for a,b,kind in segments:
        degree[a]+=1;degree[b]+=1
        assert (ps[a][0]==ps[b][0])!=(ps[a][1]==ps[b][1])
    assert max(degree)<=4
    occupied={}
    for index,(a,b,kind) in enumerate(segments):
        x,y=ps[a];u,v=ps[b];dx=(u>x)-(u<x);dy=(v>y)-(v<y)
        for t in range(abs(x-u)+abs(y-v)+1):
            point=(x+t*dx,y+t*dy)
            for other,c,d in occupied.get(point,()):
                assert point in (tuple(ps[a]),tuple(ps[b])) and point in (tuple(ps[c]),tuple(ps[d])) and set((a,b))&set((c,d))
            occupied.setdefault(point,[]).append((index,a,b))
    print(json.dumps({'event':'network','file':file.name,'max_degree':max(degree),'segments':len(segments),'grid_sites':len(occupied),'noncrossing':True}),flush=True)
