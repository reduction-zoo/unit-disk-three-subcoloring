import json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[2]
q=F(749,10000)
step=1535
raw=json.loads((root/'rounds/017/equality.json').read_text())
epoints=[[F(*v) for v in p] for p in raw['centers']]
a,b=epoints[-2:];dx,dy=b[0]-a[0],b[1]-a[1];dd=dx*dx+dy*dy
E=[(((p[0]-a[0])*dx+(p[1]-a[1])*dy)/dd,(dx*(p[1]-a[1])-dy*(p[0]-a[0]))/dd) for p in epoints[:-2]]
raw=json.loads((root/'rounds/012/gadget.json').read_text())
ipoints=[[F(*v) for v in p] for p in raw['centers']]
I=[((p[0]-ipoints[-2][0])*F(27,2),(p[1]-ipoints[-2][1])*F(27,2)) for p in ipoints[:-2]]


def construct(network,emit):
    terminals={};count=0
    def point(p):
        nonlocal count
        index=count;count+=1;emit(tuple(q*v for v in p));return index
    def terminal(p):
        if p not in terminals:terminals[p]=point(p)
        return terminals[p]
    def equality(start,direction,length,reverse):
        dx,dy=direction;end=tuple(start[j]+length*direction[j] for j in range(2))
        terminal(start);terminal(end)
        for x,y in E:
            if reverse:x,y=1-x,-y
            point((start[0]+length*(dx*x-dy*y),start[1]+length*(dy*x+dx*y)))
        return end
    def inequality(start,direction):
        dx,dy=direction;end=tuple(start[j]+27*direction[j] for j in range(2))
        terminal(start);terminal(end)
        for x,y in I:point((start[0]+dx*x-dy*y,start[1]+dy*x+dx*y))
        return end
    positions=[tuple(step*v for v in p) for p in network['points']]
    for p in sorted(positions):
        for direction in ((1,0),(0,1),(-1,0),(0,-1)):equality(p,direction,52,True)
    for u,v,kind in network['segments']:
        a,b=positions[u],positions[v];delta=tuple(b[j]-a[j] for j in range(2))
        assert (delta[0]==0)!=(delta[1]==0)
        distance=sum(abs(x) for x in delta);assert distance%step==0
        units=distance//step;assert units>=1
        direction=tuple((x>0)-(x<0) for x in delta)
        start=tuple(a[j]+52*direction[j] for j in range(2))
        unequal=kind=='ne';assert kind in ('eq','ne')
        lengths=([52]*27 if unequal else [53]*27)+([52,52]+[53]*27)*(units-1)
        for k,length in enumerate(lengths):
            if unequal and k==13:start=inequality(start,direction)
            start=equality(start,direction,length,not (unequal and k in (13,14)))
        assert start==tuple(b[j]-52*direction[j] for j in range(2))
    return [terminals[p] for p in positions],count
