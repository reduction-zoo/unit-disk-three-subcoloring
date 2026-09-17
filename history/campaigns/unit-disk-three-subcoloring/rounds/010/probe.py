import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/008/critical.json').read_text())
a=check.graph(t)
records=[json.loads(s) for s in (root/'rounds/009/output.jsonl').read_text().splitlines()]
for r in records:
    if r['status']!='unsat':
        continue
    ids=[i for i in range(34) if i!=r['removed']]
    adj=[[a[i][j] for j in ids] for i in ids]
    q,vs=check.color_solver(adj)
    i,j=[ids.index(v) for v in r['pair']]
    q.add(vs[i]==0,vs[j]==(1 if r['same'] else 0))
    for v in (i,j):
        q.add([vs[v]!=vs[u] for u in range(33) if adj[v][u]])
    status=q.check()
    out={'removed':r['removed'],'pair':r['pair'],'same':not r['same'],'status':str(status)}
    if status==z3.sat:
        w=[q.model().eval(v).as_long() for v in vs]
        assert check.valid_coloring(adj,w)
        assert all(w[v]!=w[u] for v in (i,j) for u in range(33) if adj[v][u])
        out['witness']=w
    elif status!=z3.unsat:
        raise RuntimeError(str(status))
    print(json.dumps(out),flush=True)
