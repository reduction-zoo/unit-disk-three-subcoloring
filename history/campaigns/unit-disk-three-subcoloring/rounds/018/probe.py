import itertools
import json
import sys
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'work'))
import check
import z3
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/017/equality.json').read_text())
local=check.centers(t); original=check.graph(t)
base_w=json.loads((root/'rounds/017/witness.json').read_text())
a,b=local[-2:];d=[b[j]-a[j] for j in range(2)];dd=sum(v*v for v in d)
states=list(itertools.product((False,True),(False,True),(False,True)))


def single(state):
    reverse,reflect,swap=state
    points=[]
    for p in local[:-2]:
        q=[p[j]-a[j] for j in range(2)]
        if reverse:
            q=[d[j]-q[j] for j in range(2)]
        if reflect:
            dot=sum(q[j]*d[j] for j in range(2))
            q=[2*dot*d[j]/dd-q[j] for j in range(2)]
        points.append(q)
    mapping={1:0,0:2 if swap else 1,2:1 if swap else 2}
    return points,[mapping[c] for c in base_w[:-2]]


def chain(pattern):
    n=len(pattern)
    points=[[k*v for v in d] for k in range(n+1)]
    w=[0]*(n+1); copies=[]
    for k,state in enumerate(pattern):
        ps,cs=single(state)
        ids=list(range(len(points),len(points)+33))
        points.extend([[p[j]+k*d[j] for j in range(2)] for p in ps]);w.extend(cs)
        copies.append(ids+[k,k+1])
    target={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    adj=check.graph(target)
    # Reversing equal ports swaps their local identities.
    for state,ids in zip(pattern,copies):
        if state[0]:
            ids[-2:]=ids[-2:][::-1]
        assert [[adj[i][j] for j in ids] for i in ids]==original
    valid=check.valid_coloring(adj,w)
    clean=valid and all(w[i]!=w[j] for i in range(n+1) for j in range(len(adj)) if adj[i][j])
    return target,w,clean


if __name__=='__main__':
    q,vs=check.color_solver(original)
    q.add(vs[-2]!=vs[-1])
    assert q.check()==z3.unsat
    print(json.dumps({'event':'unpinned_unequal','status':'unsat'}),flush=True)
    for state in states:
        ps,_=single(state)
        projections=[sum(p[j]*d[j] for j in range(2))/dd for p in ps]+[F(0),F(1)]
        assert min(projections)>=0 and max(projections)<=1
    assert dd>1
    print(json.dumps({'event':'projection','range':[0,1],'step_squared':[dd.numerator,dd.denominator]}),flush=True)
    good={}
    for i,j in itertools.product(range(8),repeat=2):
        _,_,valid=chain([states[i],states[j]])
        good[i,j]=valid
        print(json.dumps({'event':'pair','states':[i,j],'clean_valid':valid}),flush=True)
    for i,j in itertools.product(range(8),repeat=2):
        if not good[i,j] or not good[j,i]:
            continue
        t1,w1,v1=chain([states[i],states[j],states[i]])
        t2,w2,v2=chain([states[j],states[i],states[j]])
        print(json.dumps({'event':'triple','states':[i,j],'clean_valid':[v1,v2]}),flush=True)
        if v1 and v2:
            Path(__file__).with_name('pattern.json').write_text(json.dumps([states[i],states[j]]))
            Path(__file__).with_name('three-copy.json').write_text(json.dumps(t1))
            Path(__file__).with_name('witness.json').write_text(json.dumps(w1))
            print(json.dumps({'event':'first_success','states':[i,j]}),flush=True)
            break
    else:
        print(json.dumps({'event':'exhausted'}),flush=True)
