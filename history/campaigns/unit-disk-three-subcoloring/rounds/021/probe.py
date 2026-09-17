import importlib.util
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('junction_probe',root/'rounds/019/probe.py')
junction=importlib.util.module_from_spec(spec);spec.loader.exec_module(junction)
wire=junction.wire
ps,cs=wire.single(wire.states[4])
d=wire.d;dd=wire.dd
u=[sum(p[j]*d[j] for j in range(2))/dd for p in ps]+[wire.F(0),wire.F(1)]
v=[(d[0]*p[1]-d[1]*p[0])/dd for p in ps]+[wire.F(0)]
M=max(abs(x) for x in v)
assert min(u)>=0 and max(u)<=1
bound=(1-M)**2*dd
print(json.dumps({'event':'bounds','lateral_max':str(M),'cross_arm_distance_squared_lower_bound':str(bound),'exceeds_four':bound>4}),flush=True)
for length in (2,3):
    points=[[wire.F(0),wire.F(0)]]
    terminals=[[0]+list(range(1+k*length,1+(k+1)*length)) for k in range(4)]
    for k in range(4):
        points.extend([junction.rotate([n*x for x in d],k) for n in range(1,length+1)])
    w=[0]*len(points);copies=[]
    for k in range(4):
        for n in range(length):
            ids=list(range(len(points),len(points)+33))
            points.extend([junction.rotate([p[j]+n*d[j] for j in range(2)],k) for p in ps]);w.extend(cs)
            copies.append(ids+[terminals[k][n+1],terminals[k][n]])
    t={'centers':[[[x.numerator,x.denominator] for x in p] for p in points]}
    adj=wire.check.graph(t)
    assert all([[adj[i][j] for j in ids] for i in ids]==wire.original for ids in copies)
    valid=wire.check.valid_coloring(adj,w)
    clean=valid and all(w[i]!=w[j] for i in range(1+4*length) for j in range(len(adj)) if adj[i][j])
    print(json.dumps({'event':'extension','length':length,'vertices':len(points),'valid':valid,'clean':clean}),flush=True)
    if clean:
        Path(__file__).with_name(f'arms-{length}.json').write_text(json.dumps(t))
        Path(__file__).with_name(f'witness-{length}.json').write_text(json.dumps(w))
