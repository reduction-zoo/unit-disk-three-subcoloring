import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'work'))
import check
import z3

t = {'centers': [[[i,2],[j,2]] for i in range(4) for j in range(4)]}
adj = check.graph(t)
q, vs = check.color_solver(adj)
for i, j in itertools.combinations(range(16),2):
    for same in (True,False):
        q.push()
        q.add(vs[i] == 0, vs[j] == (0 if same else 1))
        status = q.check()
        out = {'pair':[i,j], 'same':same,'status':str(status)}
        if status == z3.sat:
            w = [q.model().eval(v).as_long() for v in vs]
            assert check.valid_coloring(adj,w)
            out['witness'] = w
        elif status != z3.unsat:
            raise RuntimeError(str(status))
        print(json.dumps(out),flush=True)
        q.pop()
