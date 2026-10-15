import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import csr_matrix
import z3
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('p',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
points,scale=p.load_points(r.parent/'051/target.json')
copies=json.loads((r.parent/'051/copies.json').read_text())
w=json.loads((r.parent/'053/witness.json').read_text())
base={'eq':json.loads((p.root/'rounds/017/witness.json').read_text())}
raw=json.loads((p.root/'rounds/012/gadget.json').read_text())
base['ne']=next(x['clean'] for x in map(json.loads,(p.root/'rounds/012/output.jsonl').read_text().splitlines()) if x['event']=='joint' and x['ports']==raw['centers'][-2:])
pairs=cKDTree(points).query_pairs(float(scale),p=np.inf,output_type='ndarray')
delta=points[pairs[:,0]]-points[pairs[:,1]]
pairs=pairs[np.sum(delta*delta,axis=1)<=scale*scale];del delta
u,v=pairs.T
adj=csr_matrix((np.ones(2*len(u),dtype=np.int8),(np.concatenate((u,v)),np.concatenate((v,u)))),shape=(len(points),len(points)))
adj.sort_indices()
def neighbors(i):return adj.indices[adj.indptr[i]:adj.indptr[i+1]]
selected=[]
for kind in ('eq','ne'):
    indices=[i for i,(k,ids) in enumerate(copies) if k==kind]
    selected.extend(indices[j] for j in (0,len(indices)//3,2*len(indices)//3,len(indices)-1))
source=json.loads((r.parent/'051/source.json').read_text())
for index in selected:
    kind,ids=copies[index];mutable=set(ids)
    centers=mutable|{int(v) for i in ids for v in neighbors(i)}
    triples=set()
    for b in centers:
        for a,c in itertools.combinations(neighbors(b),2):
            if not (a in mutable or b in mutable or c in mutable):continue
            ns=neighbors(a);j=np.searchsorted(ns,c)
            if j==len(ns) or ns[j]!=c:triples.add(tuple(sorted((int(a),int(b),int(c)))))
    for mode in ('noncanonical','nonclean'):
        colors={i:z3.Int(f'c{i}') for i in ids};q=z3.Solver()
        q.add(*[z3.And(c>=0,c<3) for c in colors.values()])
        def value(i):return colors[i] if i in colors else z3.IntVal(w[i])
        for a,b,c in triples:q.add(z3.Or(value(a)!=value(b),value(b)!=value(c)))
        if mode=='noncanonical':
            for perm in itertools.permutations(range(3)):
                q.add(z3.Or([colors[i]!=perm[c] for i,c in zip(ids,base[kind])]))
        else:q.add(z3.Or([value(a)==value(int(b)) for a in ids[-2:] for b in neighbors(a)]))
        status=q.check();assert status in (z3.sat,z3.unsat)
        recovery=False
        if status==z3.sat:
            changed={i:q.model().eval(c).as_long() for i,c in colors.items()}
            result=w.copy()
            for i,c in changed.items():result[i]=c
            assert all(len({result[a],result[b],result[c]})>1 for a,b,c in triples)
            request={'source':source,'target_solution':result}
            recovered=json.loads(subprocess.run([sys.executable,str(p.root/'work/algorithm.py'),'--extract'],input=json.dumps(request),capture_output=True,text=True,check=True).stdout)
            assignment=recovered['assignment']
            assert all(any(assignment.get(str(abs(v)),False)==(v>0) for v in clause) for clause in source['clauses'])
            (r/f'{index}-{mode}-changes.json').write_text(json.dumps({'baseline':'../053/witness.json','changed_colors':changed,'recovered':recovered}))
            recovery=True
        print(json.dumps({'copy':index,'kind':kind,'mode':mode,'affected_p3':len(triples),'status':str(status),'recovery_valid':recovery}),flush=True)
