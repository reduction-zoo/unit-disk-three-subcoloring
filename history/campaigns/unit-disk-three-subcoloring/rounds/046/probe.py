import json
from pathlib import Path
r=Path(__file__).parent
for path in sorted((r.parent/'045').glob('*-network.json')):
    net=json.loads(path.read_text());old=net['points']
    ranks=[{v:i for i,v in enumerate(sorted({p[k] for p in old}))} for k in range(2)]
    net['points']=[[ranks[k][p[k]] for k in range(2)] for p in old]
    ps=net['points'];occupied={};degree=[0]*len(ps)
    for a,b,kind in net['segments']:
        degree[a]+=1;degree[b]+=1
        x,y=ps[a];u,v=ps[b];dx=(u>x)-(u<x);dy=(v>y)-(v<y)
        assert (dx==0)!=(dy==0)
        for t in range(abs(x-u)+abs(y-v)+1):
            p=(x+t*dx,y+t*dy)
            for c,d in occupied.get(p,()):
                assert p in (tuple(ps[a]),tuple(ps[b])) and p in (tuple(ps[c]),tuple(ps[d])) and set((a,b))&set((c,d))
            occupied.setdefault(p,[]).append((a,b))
    assert max(degree)<=4
    length=sum(abs(ps[a][0]-ps[b][0])+abs(ps[a][1]-ps[b][1]) for a,b,k in net['segments'])
    count=137*len(ps)+374*length-69*len(net['segments'])+34*sum(k=='ne' for a,b,k in net['segments'])
    (r/path.name).write_text(json.dumps(net))
    print(json.dumps({'case':path.stem,'vertices':len(ps),'grid_length':length,'projected_short_target':count,'geometry_premises':True}),flush=True)
