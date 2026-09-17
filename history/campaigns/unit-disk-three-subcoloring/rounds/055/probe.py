import importlib.util
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('p',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

def query(ps,scale):
    ps=np.array(ps,dtype=np.int64).reshape(-1,2)
    pairs=cKDTree(ps).query_pairs(float(scale),p=np.inf,output_type='ndarray')
    delta=ps[pairs[:,0]]-ps[pairs[:,1]]
    return {tuple(map(int,e)) for e in pairs[np.sum(delta*delta,axis=1)<=scale*scale]}

count=0
base=list(itertools.product(range(3),repeat=2))
for mask in range(1<<9):
    ps=[p for i,p in enumerate(base) if mask>>i&1]
    expected={(i,j) for i in range(len(ps)) for j in range(i+1,len(ps)) if sum((int(a)-int(b))**2 for a,b in zip(ps[i],ps[j]))<=4}
    assert query(ps,2)==expected;count+=1
S=39400000
for delta in (-1,0,1):
    ps=[(2**45,-2**45),(2**45+S+delta,-2**45)]
    assert query(ps,S)==({(0,1)} if delta<=0 else set());count+=1
assert query([(0,0),(0,0)],S)=={(0,1)};count+=1
comparisons=0
for n in range(5):
    possible=list(itertools.combinations(range(n),2))
    for mask in range(1<<len(possible)):
        edges=[e for i,e in enumerate(possible) if mask>>i&1];es=set(edges)
        for colors in itertools.product(range(3),repeat=n):
            mono=[(a,b) for a,b in edges if colors[a]==colors[b]]
            a=[x for e in mono for x in e];b=[x for e in mono for x in e[::-1]]
            graph=csr_matrix((np.ones(len(a)),(a,b)),shape=(n,n))
            k,labels=connected_components(graph,directed=False)
            sizes=np.bincount(labels,minlength=k)
            edge_count=np.bincount([labels[a] for a,b in mono],minlength=k)
            observed=bool(np.all(edge_count==sizes*(sizes-1)//2))
            expected=not any(colors[a]==colors[b]==colors[c] and sum(e in es for e in itertools.combinations((a,b,c),2))==2 for a,b,c in itertools.combinations(range(n),3))
            assert observed==expected;comparisons+=1
(r/'empty.json').write_text('{"centers":[]}')
ps,scale=p.load_points(r/'empty.json');assert ps.shape==(0,2) and scale==1
bad=[{'centers':{}},{'centers':''}, {}, {'centers':[[[0,0],[0,1]]]}, {'centers':[[[True,1],[0,1]]]}, {'centers':[[[0.0,1],[0,1]]]}, {'centers':[[[0,-1],[0,1]]]}]
for i,t in enumerate(bad):
    file=r/f'malformed-{i}.json';file.write_text(json.dumps(t))
    try:p.load_points(file)
    except AssertionError:pass
    else:raise AssertionError('malformed target accepted')
print(json.dumps({'geometric_graph_comparisons':count,'coloring_predicate_comparisons':comparisons,'empty_target':True,'malformed_rejected':len(bad),'oracle_repair':'empty array shape and empty maximum'}))
