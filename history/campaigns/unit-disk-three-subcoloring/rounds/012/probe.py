import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/008/critical.json').read_text())
base=[p for i,p in enumerate(t['centers']) if i!=3]
records=[json.loads(s) for s in (root/'rounds/011/output.jsonl').read_text().splitlines()]
left=[r['point'] for r in records if r.get('clean') and r['status']=='sat' and r['color']==2]
right=[r['point'] for r in records if r.get('clean') and r['status']=='sat' and r['color']==1]

def query(ps,same,clean):
    adj=check.graph({'centers':ps})
    q,vs=check.color_solver(adj)
    q.add(vs[-2]==0,vs[-1]==(0 if same else 1))
    if clean:
        for v in (len(ps)-2,len(ps)-1):
            q.add([vs[v]!=vs[u] for u in range(len(ps)) if adj[v][u]])
    status=q.check()
    if status==z3.unsat:
        return None
    if status!=z3.sat:
        raise RuntimeError(str(status))
    w=[q.model().eval(v).as_long() for v in vs]
    assert check.valid_coloring(adj,w)
    assert (w[-2]==w[-1])==same
    if clean:
        assert all(w[v]!=w[u] for v in (len(ps)-2,len(ps)-1) for u in range(len(ps)) if adj[v][u])
    return w

success=[]
for l,r in itertools.product(left,right):
    ps=base+[l,r]
    ws=[query(ps,same,clean) for same,clean in ((True,False),(False,False),(False,True))]
    print(json.dumps({'event':'joint','ports':[l,r],'equal':ws[0],'different':ws[1],'clean':ws[2]}),flush=True)
    if ws[0] is None and ws[2] is not None:
        success.append((l,r))
preferred=([[2,5],[-2,5]],[[12,5],[-2,5]])
assert preferred in success
l,r=preferred
ids=list(range(33))
for v in range(33):
    trial=[i for i in ids if i!=v]
    ps=[base[i] for i in trial]+[l,r]
    clean=query(ps,False,True)
    equal=query(ps,True,False)
    keep=clean is not None and equal is None
    print(json.dumps({'event':'deletion','vertex':v,'kept':keep,'clean':clean,'equal':equal}),flush=True)
    if keep:
        ids=trial
ps=[base[i] for i in ids]+[l,r]
Path(__file__).with_name('gadget.json').write_text(json.dumps({'centers':ps}))
print(json.dumps({'event':'complete','size':len(ps),'core_indices':ids,'terminals':[len(ps)-2,len(ps)-1]}),flush=True)
