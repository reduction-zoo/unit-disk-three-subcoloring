import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire


def rotate(p,k):
    x,y=p
    for _ in range(k):
        x,y=-y,x
    return [x,y]


def junction(arms):
    points=[[wire.F(0),wire.F(0)]]+[rotate(wire.d,k) for k,_ in arms]
    w=[0]*len(points);copies=[]
    for terminal,(k,state_id) in enumerate(arms,1):
        state=wire.states[state_id]
        ps,cs=wire.single(state)
        ids=list(range(len(points),len(points)+33))
        points.extend([rotate(p,k) for p in ps]);w.extend(cs)
        pair=[0,terminal]
        if state[0]:
            pair.reverse()
        copies.append(ids+pair)
    t={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    adj=wire.check.graph(t)
    assert all([[adj[i][j] for j in ids] for i in ids]==wire.original for ids in copies)
    valid=wire.check.valid_coloring(adj,w)
    clean=valid and all(w[i]!=w[j] for i in range(len(arms)+1) for j in range(len(adj)) if adj[i][j])
    return t,w,clean


if __name__=='__main__':
    usable=[]
    for i,state in enumerate(wire.states):
        _,_,valid=wire.chain([state]*3)
        print(json.dumps({'event':'straight_state','state':i,'clean_valid':valid}),flush=True)
        if valid:
            usable.append(i)
    assert 0 in usable
    compatibility={}
    for a,b in itertools.combinations(range(4),2):
        for i,j in itertools.product(([0] if a==0 else usable),usable):
            _,_,valid=junction([(a,i),(b,j)])
            compatibility[a,i,b,j]=valid
            print(json.dumps({'event':'pair','arms':[[a,i],[b,j]],'clean_valid':valid}),flush=True)
    full=0
    for rest in itertools.product(usable,repeat=3):
        ss=(0,)+rest
        if not all(compatibility[a,ss[a],b,ss[b]] for a,b in itertools.combinations(range(4),2)):
            continue
        t,w,valid=junction(list(enumerate(ss)));full+=1
        print(json.dumps({'event':'full','states':ss,'clean_valid':valid}),flush=True)
        if valid:
            Path(__file__).with_name('junction.json').write_text(json.dumps(t))
            Path(__file__).with_name('witness.json').write_text(json.dumps(w))
            Path(__file__).with_name('states.json').write_text(json.dumps(ss))
            print(json.dumps({'event':'first_success','full_checks':full}),flush=True)
            break
    else:
        print(json.dumps({'event':'exhausted','full_checks':full}),flush=True)
