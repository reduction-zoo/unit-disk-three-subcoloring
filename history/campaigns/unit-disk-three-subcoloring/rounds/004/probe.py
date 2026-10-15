import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
for size in (1,2,3,4):
    adj=[[i//size != j//size for j in range(4*size)] for i in range(4*size)]
    w=check.solve_coloring(adj)
    if size<=3:
        explicit=[i%size for i in range(4*size)]
        assert check.valid_coloring(adj,explicit)
    else:
        assert w is None
    print(json.dumps({'bag_size':size,'status':'unsat' if w is None else 'sat','witness':w}))
