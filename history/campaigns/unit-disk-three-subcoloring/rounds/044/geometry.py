import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
root=Path(__file__).resolve().parents[2]
q=F(749,10000)
step=581
E=[]
for state in wire.states:
    ps,cs=wire.single(state)
    E.append(([(sum(p[j]*wire.d[j] for j in range(2))/wire.dd,(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd) for p in ps],cs))
I=json.loads((root/'rounds/012/gadget.json').read_text())
ip=wire.check.centers(I)
iw=next(r['clean'] for r in map(json.loads,(root/'rounds/012/output.jsonl').read_text().splitlines()) if r['event']=='joint' and r['ports']==I['centers'][-2:])


class Drawing:
    def __init__(self):
        self.points=[];self.colors=[];self.terminals={};self.copies=[]

    def terminal(self,p,color):
        p=tuple(q*v for v in p)
        if p in self.terminals:
            i=self.terminals[p];assert self.colors[i]==color
            return i
        i=len(self.points);self.terminals[p]=i
        self.points.append(p);self.colors.append(color)
        return i

    def equality(self,start,direction,length,state,color,perm=None):
        perm=tuple((i+color)%3 for i in range(3)) if perm is None else perm
        dx,dy=direction
        end=tuple(start[j]+length*direction[j] for j in range(2))
        ports=[self.terminal(start,perm[0]),self.terminal(end,perm[0])]
        ps,cs=E[state];ids=[]
        for (x,y),c in zip(ps,cs):
            ids.append(len(self.points));self.points.append((q*(start[0]+length*(x*dx-y*dy)),q*(start[1]+length*(x*dy+y*dx))))
            self.colors.append(perm[c])
        if wire.states[state][0]:ports.reverse()
        self.copies.append(('eq',ids+ports))
        return end

    def inequality(self,start,direction,perm):
        dx,dy=direction
        end=tuple(start[j]+27*direction[j] for j in range(2))
        ports=[self.terminal(start,perm[0]),self.terminal(end,perm[1])];ids=[]
        for p,c in zip(ip[:-2],iw[:-2]):
            x=(p[0]-ip[-2][0])*F(27,2);y=(p[1]-ip[-2][1])*F(27,2)
            ids.append(len(self.points));self.points.append((q*(start[0]+dx*x-dy*y),q*(start[1]+dy*x+dx*y)));self.colors.append(perm[c])
        self.copies.append(('ne',ids+ports))
        return end

    def hub(self,p,color):
        for direction in ((1,0),(0,1),(-1,0),(0,-1)):
            self.equality(p,direction,52,4,color)

    def segment(self,a,b,unequal,ca,cb):
        delta=(b[0]-a[0],b[1]-a[1]);units=(abs(delta[0])+abs(delta[1]))//step
        assert (delta[0]==0)!=(delta[1]==0) and units>=1 and sum(abs(x) for x in delta)==units*step
        direction=tuple((x>0)-(x<0) for x in delta)
        start=tuple(a[j]+52*direction[j] for j in range(2))
        extra=[52,52]+[53]*9
        lengths=([50]*9 if unequal else [53]*9)+extra*(units-1)
        if unequal:
            assert ca!=cb
            perm=(ca,cb,3-ca-cb)
        else:assert ca==cb
        for k,length in enumerate(lengths):
            if unequal and k==4:start=self.inequality(start,direction,perm)
            color=ca if not unequal or k<4 else cb
            state=4;cell_perm=None
            if unequal and k in (2,3):state=5;cell_perm=perm
            if unequal and k in (4,5):state=0;cell_perm=(perm[1],perm[2],perm[0])
            start=self.equality(start,direction,length,state,color,cell_perm)
        assert start==tuple(b[j]-52*direction[j] for j in range(2))

    def target(self):
        return {'centers':[[[v.numerator,v.denominator] for v in p] for p in self.points]}


def adjacency(points):
    scale=math.lcm(*(v.denominator for p in points for v in p))
    ps=[tuple(int(v*scale) for v in p) for p in points];buckets={};adj=[set() for p in ps]
    for i,(x,y) in enumerate(ps):
        cell=(x//scale,y//scale)
        for dx,dy in itertools.product((-1,0,1),repeat=2):
            for j in buckets.get((cell[0]+dx,cell[1]+dy),()):
                u,v=ps[j]
                if (x-u)**2+(y-v)**2<=scale**2:adj[i].add(j);adj[j].add(i)
        buckets.setdefault(cell,[]).append(i)
    return adj


def validate(points,colors):
    adj=adjacency(points)
    for b,ns in enumerate(adj):
        same=[a for a in ns if colors[a]==colors[b]]
        for a,c in itertools.combinations(same,2):
            if c not in adj[a]:return False,(a,b,c),adj
    return True,None,adj
