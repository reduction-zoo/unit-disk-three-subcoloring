import itertools
import json
import sys
from pathlib import Path
import network
sys.path.insert(0,str(network.root/'work'))
import check
import z3
r=Path(__file__).parent
for case in json.loads((network.root/'work/cases.json').read_text()):
    s=case['source'];net=network.construct(s)
    c=[z3.Int(f'c{i}') for i in range(len(net['points']))];q=z3.Solver()
    q.add(*[z3.And(v>=0,v<3) for v in c])
    for a,b,kind in net['segments']:q.add(c[a]==c[b] if kind=='eq' else c[a]!=c[b])
    result=q.check();assert result in (z3.sat,z3.unsat)
    assert (result==z3.sat)==case['yes']==(check.source_solve(s) is not None)
    recovered=0
    if result==z3.sat:
        w=[q.model().eval(v).as_long() for v in c]
        for perm in itertools.permutations(range(3)):
            assert check.source_witness(s,network.extract(s,net,[perm[v] for v in w]));recovered+=1
        (r/(case['name']+'-witness.json')).write_text(json.dumps(w))
    (r/(case['name']+'-network.json')).write_text(json.dumps(net))
    print(json.dumps({'case':case['name'],'status':str(result),'vertices':len(c),'segments':len(net['segments']),'crossings':net['crossings'],'intermediate_recoveries':recovered}),flush=True)

for case in json.loads((network.root/'work/cases.json').read_text()):
    net=network.construct(case['source']);ps=net['points'];occupied={};degree=[0]*len(ps)
    for index,(a,b,kind) in enumerate(net['segments']):
        degree[a]+=1;degree[b]+=1
        x,y=ps[a];u,v=ps[b];dx=(u>x)-(u<x);dy=(v>y)-(v<y)
        assert (dx==0)!=(dy==0)
        for t in range(abs(x-u)+abs(y-v)+1):
            point=(x+t*dx,y+t*dy)
            for c,d in occupied.get(point,()):
                assert point in (tuple(ps[a]),tuple(ps[b])) and point in (tuple(ps[c]),tuple(ps[d])) and set((a,b))&set((c,d))
            occupied.setdefault(point,[]).append((a,b))
    assert max(degree)<=4
    length=sum(abs(ps[a][0]-ps[b][0])+abs(ps[a][1]-ps[b][1]) for a,b,k in net['segments'])
    constant=137*len(ps)-69*len(net['segments'])+34*sum(k=='ne' for a,b,k in net['segments'])
    print(json.dumps({'event':'geometry_premises','case':case['name'],'max_degree':max(degree),'projected_old_spacing':constant+986*length,'projected_short_spacing':constant+374*length}),flush=True)
