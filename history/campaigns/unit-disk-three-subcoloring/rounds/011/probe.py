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
for y in range(1,5):
    for x in range(15):
        point=[[x,5],[-y,5]]
        adj=check.graph({'centers':base+[point]})
        q,vs=check.color_solver(adj)
        q.add([vs[ids.index(v)]==col for col,v in enumerate((0,4,18))])
        feasible=[]
        for col in range(3):
            q.push();q.add(vs[-1]==col)
            status=q.check()
            out={'point':point,'color':col,'status':str(status)}
            if status==z3.sat:
                w=[q.model().eval(v).as_long() for v in vs]
                assert check.valid_coloring(adj,w)
                feasible.append(col)
                out['witness']=w
            elif status!=z3.unsat:
                raise RuntimeError(str(status))
            print(json.dumps(out),flush=True)
            q.pop()
        if len(feasible)==1:
            q.add(vs[-1]==feasible[0])
            q.add([vs[-1]!=vs[i] for i in range(33) if adj[-1][i]])
            status=q.check()
            out={'point':point,'clean':True,'color':feasible[0],'status':str(status)}
            if status==z3.sat:
                w=[q.model().eval(v).as_long() for v in vs]
                assert check.valid_coloring(adj,w)
                assert all(w[-1]!=w[i] for i in range(33) if adj[-1][i])
                out['witness']=w
            elif status!=z3.unsat:
                raise RuntimeError(str(status))
            print(json.dumps(out),flush=True)
