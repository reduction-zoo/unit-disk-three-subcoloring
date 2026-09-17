from fractions import Fraction
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
gadget=json.loads((root/'rounds/012/gadget.json').read_text())
local=check.centers(gadget)
local_adj=check.graph(gadget)
rows=[json.loads(s) for s in (root/'rounds/012/output.jsonl').read_text().splitlines()]
canonical=next(r['clean'] for r in rows if r['event']=='joint' and r['ports']==gadget['centers'][-2:])

def compose(terminals,edges,reverse,flips):
    points=[[Fraction(x),Fraction(y)] for x,y in terminals]
    copies=[]
    for e,(i,j) in enumerate(edges):
        if reverse[e]:
            i,j=j,i
        a,b=points[i],points[j]
        dx,dy=b[0]-a[0],b[1]-a[1]
        ids=[]
        for x,y in local[:-2]:
            u=(x-local[-2][0])/2
            v=(y-local[-2][1])/2*flips[e]
            ids.append(len(points))
            points.append([a[0]+u*dx-v*dy,a[1]+u*dy+v*dx])
        copies.append(ids+[i,j])
    target={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    adj=check.graph(target)
    assert all([[adj[i][j] for j in ids] for i in ids]==local_adj for ids in copies)
    return target,adj,copies

def lift(adj,copies,colors):
    w=list(colors)+[-1]*(len(adj)-len(colors))
    for ids in copies:
        a,b=colors[ids[-2]],colors[ids[-1]]
        assert a!=b
        mapping={0:a,1:b,2:3-a-b}
        for v,c in zip(ids,canonical):
            w[v]=mapping[c]
    return w if check.valid_coloring(adj,w) else None

def solve(adj,colors,clean):
    q,vs=check.color_solver(adj)
    q.add([vs[i]==c for i,c in enumerate(colors)])
    if clean:
        q.add([vs[i]!=vs[j] for i in range(len(colors)) for j in range(len(adj)) if adj[i][j]])
    status=q.check()
    if status==z3.unsat:
        return None
    if status!=z3.sat:
        raise RuntimeError(str(status))
    w=[q.model().eval(v).as_long() for v in vs]
    assert check.valid_coloring(adj,w)
    assert w[:len(colors)]==list(colors)
    if clean:
        assert all(w[i]!=w[j] for i in range(len(colors)) for j in range(len(adj)) if adj[i][j])
    return w
