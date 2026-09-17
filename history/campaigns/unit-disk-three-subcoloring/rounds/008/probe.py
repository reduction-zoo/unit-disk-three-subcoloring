import itertools
import json
from pathlib import Path
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/007/obstruction.json').read_text())
# Independent integer scaling for this fixture only, not a candidate graph implementation.
assert all(p[0][1]==p[1][1]==5 for p in t['centers'])
ps=[(p[0][0],p[1][0]) for p in t['centers']]
adj=[[i!=j and (a[0]-b[0])**2+(a[1]-b[1])**2<=25 for j,b in enumerate(ps)] for i,a in enumerate(ps)]

def solve(ids,k):
    c={(v,col):z3.Bool(f'b{v}_{col}') for v in ids for col in range(k)}
    q=z3.Solver()
    for v in ids:
        q.add(z3.PbEq([(c[v,col],1) for col in range(k)],1))
    for b in ids:
        ns=[v for v in ids if adj[b][v]]
        for a,d in itertools.combinations(ns,2):
            if not adj[a][d]:
                for col in range(k):
                    q.add(z3.Or(z3.Not(c[a,col]),z3.Not(c[b,col]),z3.Not(c[d,col])))
    status=q.check()
    if status==z3.unsat:
        return None
    if status!=z3.sat:
        raise RuntimeError(str(status))
    w={v:next(col for col in range(k) if z3.is_true(q.model().eval(c[v,col]))) for v in ids}
    for vs in itertools.combinations(ids,3):
        if len({w[v] for v in vs})==1:
            assert sum(adj[a][b] for a,b in itertools.combinations(vs,2))!=2
    return w

ids=list(range(49))
assert solve(ids,3) is None
print(json.dumps({'event':'independent_baseline','status':'unsat','n':49}),flush=True)
w=solve(ids,4)
assert w is not None
print(json.dumps({'event':'four_colors','witness':w}),flush=True)
for v in range(49):
    trial=[i for i in ids if i!=v]
    print(json.dumps({'event':'start_deletion','vertex':v,'size':len(trial)}),flush=True)
    w=solve(trial,3)
    print(json.dumps({'event':'deletion','vertex':v,'kept':w is None,'size':len(trial),'witness':w}),flush=True)
    if w is None:
        ids=trial
out={'centers':[t['centers'][i] for i in ids]}
Path(__file__).with_name('critical.json').write_text(json.dumps(out))
Path(__file__).with_name('indices.json').write_text(json.dumps(ids))
print(json.dumps({'event':'complete','size':len(ids),'original_indices':ids}),flush=True)
