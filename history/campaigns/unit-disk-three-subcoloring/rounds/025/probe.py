import itertools
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'018'))
import probe as wire
root=Path(__file__).resolve().parents[2]
inequality=json.loads((root/'rounds/012/gadget.json').read_text())
i_points=wire.check.centers(inequality);i_adj=wire.check.graph(inequality)
rows=[json.loads(s) for s in (root/'rounds/012/output.jsonl').read_text().splitlines()]
i_w=next(r['clean'] for r in rows if r['event']=='joint' and r['ports']==inequality['centers'][-2:])
q=wire.F(749,10000)
L=52*q
R=53*q
S=27*q

def connector(i_state,left,right):
    points=[[x,wire.F(0)] for x in (-2*L,-L,wire.F(0),S,S+R,S+2*R)]
    colors=[0,0,0,1,1,1];copies=[]
    reverse,reflect=i_state
    ids=[]
    for p,c in zip(i_points[:-2],i_w[:-2]):
        x,y=p[0]-i_points[-2][0],p[1]-i_points[-2][1]
        if reverse:
            x,y=2-x,-y
        if reflect:
            y=-y
        ids.append(len(points));points.append([x*S/2,y*S/2])
        colors.append(({0:1,1:0,2:2} if reverse else {0:0,1:1,2:2})[c])
    copies.append((ids+([3,2] if reverse else [2,3]),i_adj))
    for side,state_id in ((-1,left),(1,right)):
        state=wire.states[state_id]
        length=L if side==-1 else R
        ps,cs=wire.single(state)
        for cell in range(2):
            ids=[]
            for p,c in zip(ps,cs):
                u=sum(p[j]*wire.d[j] for j in range(2))/wire.dd
                v=(wire.d[0]*p[1]-wire.d[1]*p[0])/wire.dd
                ids.append(len(points))
                points.append([(0 if side==-1 else S)+side*length*(cell+u),side*length*v])
                colors.append(c if side==-1 else (c+1)%3)
            terminals=[2-cell,1-cell] if side==-1 else [3+cell,4+cell]
            if state[0]:
                terminals.reverse()
            copies.append((ids+terminals,wire.original))
    t={'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}
    a=wire.check.graph(t)
    assert all([[a[i][j] for j in ids] for i in ids]==original for ids,original in copies)
    valid=wire.check.valid_coloring(a,colors)
    clean=valid and all(colors[i]!=colors[j] for i in range(6) for j in range(len(a)) if a[i][j])
    return t,colors,clean


if __name__=='__main__':
    for left_units,right_units in itertools.product((52,53),repeat=2):
        L=left_units*q;R=right_units*q
        t,w,valid=connector((False,False),1,0)
        print(json.dumps({'length_units':[left_units,right_units],'clean_valid':valid}),flush=True)
        if valid:
            Path(__file__).with_name(f'connector-{left_units}-{right_units}.json').write_text(json.dumps(t))
            Path(__file__).with_name(f'witness-{left_units}-{right_units}.json').write_text(json.dumps(w))
