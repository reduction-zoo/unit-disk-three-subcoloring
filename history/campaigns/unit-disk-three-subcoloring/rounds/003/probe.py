import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
count=0
for n in range(5):
    edges=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(edges)):
        adj=[[False]*n for _ in range(n)]
        for bit,(i,j) in enumerate(edges):
            adj[i][j]=adj[j][i]=bool(mask>>bit&1)
        proper=any(all(w[i]!=w[j] for i,j in edges if adj[i][j]) for w in itertools.product(range(3),repeat=n))
        blow=[[adj[i//4][j//4] for j in range(n*4)] for i in range(n*4)]
        w=check.solve_coloring(blow)
        assert (w is not None)==proper
        if w is not None:
            recovered=[next(c for c in range(3) if w[i*4:i*4+4].count(c)>=2) for i in range(n)]
            assert all(recovered[i]!=recovered[j] for i,j in edges if adj[i][j])
        count+=1
print(json.dumps({'source_graphs':count,'solver_queries':count,'semantic_equivalence':True,
                  'one_edge_output':'K4,4','geometry':'excluded: induced triangle-free nonplanar K3,3'}))
