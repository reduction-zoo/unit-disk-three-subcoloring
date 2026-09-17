"""Independent finite checks; imports no campaign implementation."""
import itertools as it
import json
import math
from fractions import Fraction as F
from pathlib import Path
import z3
R=Path(__file__).resolve().parents[2]
OUT=Path(__file__).parent
q=F(749,10000)
def raw(name):
    return [tuple(F(*x) for x in p) for p in json.loads((R/name).read_text())['centers']]
E=raw('rounds/017/equality.json'); I=raw('rounds/012/gadget.json')
EW=json.loads((R/'rounds/017/witness.json').read_text())
record=json.loads((R/'rounds/012/gadget.json').read_text())
IW=next(x['clean'] for x in map(json.loads,(R/'rounds/012/output.jsonl').read_text().splitlines()) if x['event']=='joint' and x['ports']==record['centers'][-2:])
def graph(ps):
    scale=math.lcm(*(x.denominator for p in ps for x in p))
    ps=[tuple(int(x*scale) for x in p) for p in ps]; buckets={}; adj=[set() for _ in ps]
    for i,(x,y) in enumerate(ps):
        cell=(x//scale,y//scale)
        for a,b in it.product((-1,0,1),repeat=2):
            for j in buckets.get((cell[0]+a,cell[1]+b),[]):
                u,v=ps[j]
                if (x-u)**2+(y-v)**2<=scale**2:adj[i].add(j);adj[j].add(i)
        buckets.setdefault(cell,[]).append(i)
    return adj
def bad(adj,cs):
    for b,ns in enumerate(adj):
        for a,c in it.combinations([a for a in ns if cs[a]==cs[b]],2):
            if c not in adj[a]:return (a,b,c)
    return None
for name,ps,w in [('eq',E,EW),('ne',I,IW)]:
    adj=graph(ps);s=z3.Solver();cs=[z3.Int(f'{name}{i}') for i in range(35)]
    s.add(*[z3.And(c>=0,c<=2) for c in cs])
    for b,ns in enumerate(adj):
        for a,c in it.combinations(ns,2):
            if c not in adj[a]:s.add(z3.Or(cs[a]!=cs[b],cs[c]!=cs[b]))
    s.add(cs[33]==0,cs[34]==(1 if name=='eq' else 0))
    assert s.check()==z3.unsat
    assert bad(adj,w) is None
    assert all(w[t]!=w[j] for t in (33,34) for j in adj[t])
    print(json.dumps({'primitive':name,'forbidden':'unsat','clean':True}),flush=True)
dx,dy=(E[34][i]-E[33][i] for i in range(2));dd=dx*dx+dy*dy
norm=[(((x-E[33][0])*dx+(y-E[33][1])*dy)/dd,(dx*(y-E[33][1])-dy*(x-E[33][0]))/dd) for x,y in E[:33]]
class Drawing:
    def __init__(self):self.ps=[];self.cs=[];self.ports={}
    def point(self,p,c,port=False):
        if port and p in self.ports:
            assert self.cs[self.ports[p]]==c
            return
        if port:self.ports[p]=len(self.ps)
        self.ps.append(p);self.cs.append(c)
    def cell(self,a,d,length,state,perm,kind='eq'):
        b=tuple(a[i]+length*d[i] for i in range(2))
        self.point(a,perm[0],True);self.point(b,perm[kind=='ne'],True)
        if kind=='eq':
            swap=state%2;reverse=state>=4
            local=[(1-x,-y) if reverse else (x,y) for x,y in norm]
            wc=[{1:0,0:2 if swap else 1,2:1 if swap else 2}[c] for c in EW[:33]]
        else:
            local=[((x-I[33][0])/2,(y-I[33][1])/2) for x,y in I[:33]];wc=IW[:33]
        for (x,y),c in zip(local,wc):
            self.point((a[0]+length*(d[0]*x-d[1]*y),a[1]+length*(d[1]*x+d[0]*y)),perm[c])
        return b
    def hub(self,p,c):
        for d in ((1,0),(0,1),(-1,0),(0,-1)):self.cell(p,d,52,4,tuple((c+i)%3 for i in range(3)))
    def wire(self,a,b,ca,cb):
        d=tuple((b[i]>a[i])-(b[i]<a[i]) for i in range(2));p=tuple(a[i]+52*d[i] for i in range(2))
        if ca==cb:
            perm=tuple((ca+i)%3 for i in range(3))
            for (x,y),state in zip(((1,0),(F(4,5),F(3,5)),(1,0),(F(4,5),F(-3,5)),(1,0)),(4,5,4,4,5)):
                p=self.cell(p,(d[0]*x-d[1]*y,d[1]*x+d[0]*y),50,state,perm)
        else:
            perm=(ca,cb,3-ca-cb)
            for length,state,k,pm in [(50,5,'eq',perm),(F(103,2),5,'eq',perm),(27,0,'ne',perm),(F(103,2),0,'eq',(cb,perm[2],ca)),(50,0,'eq',(cb,perm[2],ca))]:p=self.cell(p,d,length,state,pm,k)
        assert p==tuple(b[i]-52*d[i] for i in range(2))
for incoming in it.product((False,True),repeat=4):
    d=Drawing();d.hub((0,0),0)
    for j,dr in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
        endpoint=tuple(334*x for x in dr);c=j%3;d.hub(endpoint,c)
        if incoming[j]:d.wire(endpoint,(0,0),c,0)
        else:d.wire((0,0),endpoint,0,c)
    ps=[tuple(q*x for x in p) for p in d.ps];failure=bad(graph(ps),d.cs)
    print(json.dumps({'incoming':incoming,'vertices':len(ps),'failure':failure}),flush=True)
    if failure:
        (OUT/'counterexample.json').write_text(json.dumps({'incoming':incoming,'triple':failure,'points':[[str(x) for x in ps[i]] for i in failure],'colors':[d.cs[i] for i in failure]}))
        break
# Any P3 has diameter at most two. Check distinct arm interiors are farther
# apart than two, irrespective of direction, inequality, or local colors.
variants={}
for axis,dr in enumerate(((1,0),(0,1),(-1,0),(0,-1))):
    for incoming,unequal in it.product((False,True),repeat=2):
        d=Drawing();end=tuple(334*x for x in dr)
        if incoming:d.wire(end,(0,0),int(unequal),0)
        else:d.wire((0,0),end,0,int(unequal))
        variants[axis,incoming,unequal]=[tuple(q*x for x in p) for p in d.ps]
checks=0
for axis,other in it.combinations(range(4),2):
    for ia,ka,ib,kb in it.product((False,True),repeat=4):
        a=variants[axis,ia,ka];b=variants[other,ib,kb]
        # Dividing coordinates by two makes graph() test the distance-two bound.
        adj=graph([tuple(x/2 for x in p) for p in a+b])
        assert all(j<len(a) for i in range(len(a)) for j in adj[i])
        checks+=1
print(json.dumps({'cross_arm_interior_distance_gt_2':checks}),flush=True)
# Independently audit the finite orthogonal routing, including self-crossings.
routing=json.loads((R/'rounds/032/routing.json').read_text())
segments=[(tuple(a),tuple(b)) for path in routing['paths'] for a,b in zip(path['points'],path['points'][1:])]
for a,b in segments:assert (a[0]==b[0]) != (a[1]==b[1])
for (a,b),(c,d) in it.combinations(segments,2):
    lo=tuple(max(min(a[k],b[k]),min(c[k],d[k])) for k in (0,1))
    hi=tuple(min(max(a[k],b[k]),max(c[k],d[k])) for k in (0,1))
    if all(lo[k]<=hi[k] for k in (0,1)):
        assert lo==hi and lo in (a,b) and lo in (c,d)
nodes=sorted({p for edge in segments for p in edge});degree={p:0 for p in nodes}
for a,b in segments:degree[a]+=1;degree[b]+=1
assert max(degree.values())<=4
print(json.dumps({'routing_segments':len(segments),'junctions':len(nodes),'max_degree':max(degree.values())}),flush=True)
# Each allowed equality length and the inequality scaling preserve the raw graph.
for length in (F(50),F(103,2),F(52)):
    ps=[(length*q*x,length*q*y) for x,y in norm]+[(F(0),F(0)),(length*q,F(0))]
    assert graph(ps)==graph(E)
assert graph([tuple(x*27*q/2 for x in p) for p in I])==graph(I)
print(json.dumps({'equality_lengths_preserve_graph':3,'inequality_scale_preserves_graph':True}),flush=True)
gadgets=json.loads((R/'rounds/027/gadgets.json').read_text())
for bits in it.product((0,1),repeat=3):
    cs=[z3.Int(f'cl{i}') for i in range(9)];s=z3.Solver()
    s.add(*[z3.And(c>=0,c<3) for c in cs])
    s.add(*[cs[i]==bits[i] for i in range(3)],cs[8]==0)
    s.add(*[cs[a]!=cs[b] for a,b in gadgets['clause_edges']])
    assert (s.check()==z3.sat)==(0 in bits)
for colors in it.product(range(3),repeat=4):
    cs={p:z3.Int(f'route{i}') for i,p in enumerate(nodes)};s=z3.Solver()
    s.add(*[z3.And(c>=0,c<3) for c in cs.values()])
    for path in routing['paths']:
        for k,(a,b) in enumerate(zip(path['points'],path['points'][1:])):
            s.add(cs[tuple(a)]!=cs[tuple(b)] if k==0 and path['kind']=='ne' else cs[tuple(a)]==cs[tuple(b)])
    for port,color in zip(routing['ports'],colors):s.add(cs[tuple(routing['vertices'][str(port)])]==color)
    assert (s.check()==z3.sat)==(colors[0]==colors[2] and colors[1]==colors[3])
print(json.dumps({'clause_boundaries':8,'routed_crossover_boundaries':81}),flush=True)
