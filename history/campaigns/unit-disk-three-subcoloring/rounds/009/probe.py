import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/008/critical.json').read_text())
a=check.graph(t)
for removed in (3,9,29,33):
    ids=[i for i in range(34) if i!=removed]
    adj=[[a[i][j] for j in ids] for i in ids]
    q,vs=check.color_solver(adj)
    ns=[i for i in ids if a[removed][i]]
    assert len(ns)==8
    for i,j in itertools.combinations(ns,2):
        for same in (True,False):
            q.push()
            q.add(vs[ids.index(i)]==0,vs[ids.index(j)]==(0 if same else 1))
            status=q.check()
            out={'removed':removed,'pair':[i,j],'same':same,'status':str(status)}
            if status==z3.sat:
                w=[q.model().eval(v).as_long() for v in vs]
                assert check.valid_coloring(adj,w)
                out['witness']=w
            elif status!=z3.unsat:
                raise RuntimeError(str(status))
            print(json.dumps(out),flush=True)
            q.pop()
