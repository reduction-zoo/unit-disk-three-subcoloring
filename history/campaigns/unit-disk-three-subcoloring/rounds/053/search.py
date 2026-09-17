import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
import z3
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('projection',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)


def search(points,scale,copies,terminal_colors,output):
    assert terminal_colors is not None
    n=len(points);owner=np.full(n,-1,dtype=np.int64);low=np.full(n,-1,dtype=np.int8);high=low.copy()
    base={'eq':json.loads((p.root/'rounds/017/witness.json').read_text())}
    raw=json.loads((p.root/'rounds/012/gadget.json').read_text())
    base['ne']=next(x['clean'] for x in map(json.loads,(p.root/'rounds/012/output.jsonl').read_text().splitlines()) if x['event']=='joint' and x['ports']==raw['centers'][-2:])
    for i,c in terminal_colors.items():low[i]=high[i]=c
    variables=[]
    for kind,ids in copies:
        options=[[perm[c] for c in base[kind]] for perm in itertools.permutations(range(3)) if all(perm[base[kind][j]]==terminal_colors[ids[j]] for j in (-2,-1))]
        assert len(options)==(2 if kind=='eq' else 1)
        for values in options:
            a=p.induced(points,scale,ids)
            for b in range(35):
                ns=[j for j in range(35) if a[b,j] and values[b]==values[j]]
                assert all(a[u,v] for u,v in itertools.combinations(ns,2))
        assert np.all(low[ids[:-2]]==-1)
        low[ids[:-2]]=options[0][:-2];high[ids[:-2]]=options[-1][:-2]
        if len(options)==2:
            owner[ids[:-2]]=len(variables);variables.append(z3.Bool(f's{len(variables)}'))
    assert np.all(low>=0)
    pairs=cKDTree(points).query_pairs(float(scale),p=np.inf,output_type='ndarray')
    delta=points[pairs[:,0]]-points[pairs[:,1]]
    pairs=pairs[np.sum(delta*delta,axis=1)<=scale*scale]
    del delta
    u,v=pairs.T
    adjacency=csr_matrix((np.ones(2*len(u),dtype=np.int8),(np.concatenate((u,v)),np.concatenate((v,u)))),shape=(n,n))
    adjacency.sort_indices()
    print(json.dumps({'event':'exact_graph','vertices':n,'edges':len(u),'phase_variables':len(variables)}),flush=True)
    solver=z3.Solver()
    for attempt in range(64):
        status=solver.check()
        if status==z3.unsat:
            print(json.dumps({'event':'restricted_search','attempt':attempt+1,'target_decision':'unknown','reason':'restricted-domain UNSAT'}),flush=True);return None
        assert status==z3.sat
        phase=np.array([z3.is_true(solver.model().eval(b,model_completion=True)) for b in variables],dtype=bool)
        selected=np.zeros(n,dtype=bool);selected[owner>=0]=phase[owner[owner>=0]]
        colors=np.where(selected,high,low)
        same=colors[u]==colors[v];mu=u[same];mv=v[same]
        mono=csr_matrix((np.ones(2*len(mu),dtype=np.int8),(np.concatenate((mu,mv)),np.concatenate((mv,mu)))),shape=(n,n))
        count,labels=connected_components(mono,directed=False)
        sizes=np.bincount(labels,minlength=count);edges=np.bincount(labels[mu],minlength=count)
        bad=np.flatnonzero(edges!=sizes*(sizes-1)//2)
        print(json.dumps({'event':'phase_search','attempt':attempt+1,'bad_components':len(bad)}),flush=True)
        if not len(bad):
            output.write_text(json.dumps(colors.tolist()))
            return colors.tolist()
        order=np.argsort(labels);offset=np.concatenate(([0],np.cumsum(sizes)))
        for component in bad:
            found=False
            for b in order[offset[component]:offset[component+1]]:
                ns=mono.indices[mono.indptr[b]:mono.indptr[b+1]]
                for a,c in itertools.combinations(ns,2):
                    neighbors=adjacency.indices[adjacency.indptr[a]:adjacency.indptr[a+1]]
                    k=np.searchsorted(neighbors,c)
                    if k==len(neighbors) or neighbors[k]!=c:
                        ids=sorted({int(owner[i]) for i in (a,b,c) if owner[i]>=0})
                        solver.add(z3.Or([variables[i]!=bool(phase[i]) for i in ids]))
                        found=True;break
                if found:break
            assert found
    print(json.dumps({'event':'restricted_search','target_decision':'unknown','reason':'64-query scope exhausted'}),flush=True)
    return None


if __name__=='__main__':
    points,scale=p.load_points(r.parent/'051/target.json')
    copies=json.loads((r.parent/'051/copies.json').read_text())
    terminal_colors={int(k):v for k,v in json.loads((r.parent/'052/terminal-colors.json').read_text()).items()}
    w=search(points,scale,copies,terminal_colors,r/'witness.json')
    if w is not None:
        source=json.loads((r.parent/'051/source.json').read_text())
        for perm in itertools.permutations(range(3)):
            request={'source':source,'target_solution':[perm[c] for c in w]}
            result=json.loads(subprocess.run([sys.executable,str(p.root/'work/algorithm.py'),'--extract'],input=json.dumps(request),capture_output=True,text=True,check=True).stdout)
            assignment=result['assignment']
            assert all(any(assignment.get(str(abs(v)),False)==(v>0) for v in clause) for clause in source['clauses'])
            print(json.dumps({'event':'independent_witness_recovery','permutation':perm,'valid':True}),flush=True)
