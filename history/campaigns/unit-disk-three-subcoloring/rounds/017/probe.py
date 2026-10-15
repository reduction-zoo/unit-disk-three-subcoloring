import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/008/critical.json').read_text())
ids=[i for i in range(34) if i!=3]
base=[t['centers'][i] for i in ids]
old=[json.loads(s) for s in (root/'rounds/011/output.jsonl').read_text().splitlines()]
known={(r['point'][0][0],r['point'][1][0]) for r in old}
ports=[{'point':r['point'],'color':r['color']} for r in old if r.get('clean') and r['status']=='sat']
points=set()
for k in range(1,5):
    for v in range(15):
        points.update(((v,12+k),(2-k,v-1),(12+k,v-1)))
points-=known
queries=0

def solver(extra):
    adj=check.graph({'centers':base+extra})
    q,vs=check.color_solver(adj)
    q.add([vs[ids.index(v)]==col for col,v in enumerate((0,4,18))])
    return adj,q,vs

def result(adj,q,vs):
    global queries
    status=q.check();queries+=1
    if status==z3.unsat:
        return None
    if status!=z3.sat:
        raise RuntimeError(str(status))
    w=[q.model().eval(v).as_long() for v in vs]
    assert check.valid_coloring(adj,w)
    return w

for x,y in sorted(points):
    point=[[x,5],[y,5]]
    adj,q,vs=solver([point])
    feasible=[]
    for col in range(3):
        q.push();q.add(vs[-1]==col)
        w=result(adj,q,vs)
        print(json.dumps({'event':'color','point':point,'color':col,'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
        if w is not None:
            feasible.append(col)
        q.pop()
    if len(feasible)==1:
        q.add(vs[-1]==feasible[0])
        q.add([vs[-1]!=vs[i] for i in range(33) if adj[-1][i]])
        w=result(adj,q,vs)
        print(json.dumps({'event':'clean','point':point,'color':feasible[0],'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
        if w is not None:
            assert all(w[-1]!=w[i] for i in range(33) if adj[-1][i])
            ports.append({'point':point,'color':feasible[0]})
Path(__file__).with_name('ports.json').write_text(json.dumps(ports))
pairs=[]
for a,b in itertools.combinations(ports,2):
    dist=sum((a['point'][j][0]-b['point'][j][0])**2 for j in range(2))
    if a['color']==b['color'] and dist>25:
        pairs.append((dist,a,b))
pairs.sort(key=lambda p:(-p[0],p[1]['point'],p[2]['point']))
for dist,a,b in pairs[:12]:
    adj,q,vs=solver([a['point'],b['point']])
    q.add(vs[-2]==a['color'],vs[-1]==a['color'])
    q.add([vs[v]!=vs[i] for v in (33,34) for i in range(35) if adj[v][i]])
    w=result(adj,q,vs)
    print(json.dumps({'event':'joint','ports':[a,b],'distance_squared':[dist,25], 'status':'unsat' if w is None else 'sat','witness':w}),flush=True)
    if w is not None:
        assert all(w[v]!=w[i] for v in (33,34) for i in range(35) if adj[v][i])
        Path(__file__).with_name('equality.json').write_text(json.dumps({'centers':base+[a['point'],b['point']]}))
        Path(__file__).with_name('witness.json').write_text(json.dumps(w))
        print(json.dumps({'event':'first_success','positions':len(points),'queries':queries}),flush=True)
        break
else:
    print(json.dumps({'event':'exhausted','positions':len(points),'queries':queries,'separated_pairs':len(pairs)}),flush=True)
