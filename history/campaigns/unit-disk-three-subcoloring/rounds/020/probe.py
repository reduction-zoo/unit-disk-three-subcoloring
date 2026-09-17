import importlib.util
import itertools
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('junction_probe',root/'rounds/019/probe.py')
junction=importlib.util.module_from_spec(spec);spec.loader.exec_module(junction)
wire=junction.wire
compatibility={}
for a,b in itertools.combinations(range(4),2):
    for i,j in itertools.product(([4] if a==0 else range(8)),range(8)):
        _,_,valid=junction.junction([(a,i),(b,j)])
        compatibility[a,i,b,j]=valid
        print(json.dumps({'event':'pair','arms':[[a,i],[b,j]],'clean_valid':valid}),flush=True)
ranked=[];full=0
for rest in itertools.product(range(8),repeat=3):
    ss=(4,)+rest
    score=sum(compatibility[a,ss[a],b,ss[b]] for a,b in itertools.combinations(range(4),2))
    ranked.append((-score,ss))
    if score!=6:
        continue
    t,w,valid=junction.junction(list(enumerate(ss)));full+=1
    print(json.dumps({'event':'full','states':ss,'clean_valid':valid}),flush=True)
    if valid:
        Path(__file__).with_name('junction.json').write_text(json.dumps(t))
        Path(__file__).with_name('witness.json').write_text(json.dumps(w))
        Path(__file__).with_name('states.json').write_text(json.dumps(ss))
        print(json.dumps({'event':'canonical_success','full_checks':full,'solver_queries':0}),flush=True)
        raise SystemExit(0)
seen=set();queries=0
for negscore,ss in sorted(ranked):
    key=tuple((wire.states[i][0],wire.states[i][1]) for i in ss)
    if key in seen:
        continue
    seen.add(key)
    t,_,_=junction.junction(list(enumerate(ss)))
    adj=wire.check.graph(t)
    q,vs=wire.check.color_solver(adj)
    q.add([vs[i]==0 for i in range(5)])
    q.add([vs[i]!=vs[j] for i in range(5) for j in range(len(adj)) if adj[i][j]])
    status=q.check();queries+=1
    out={'event':'solver','states':ss,'pair_score':-negscore,'status':str(status)}
    if status==wire.z3.sat:
        w=[q.model().eval(v).as_long() for v in vs]
        assert wire.check.valid_coloring(adj,w)
        assert all(w[i]!=w[j] for i in range(5) for j in range(len(adj)) if adj[i][j])
        out['witness']=w
        Path(__file__).with_name('junction.json').write_text(json.dumps(t))
        Path(__file__).with_name('witness.json').write_text(json.dumps(w))
        Path(__file__).with_name('states.json').write_text(json.dumps(ss))
        print(json.dumps(out),flush=True)
        print(json.dumps({'event':'solver_success','full_checks':full,'solver_queries':queries}),flush=True)
        break
    if status!=wire.z3.unsat:
        raise RuntimeError(str(status))
    print(json.dumps(out),flush=True)
    if queries==8:
        print(json.dumps({'event':'exhausted','full_checks':full,'solver_queries':queries}),flush=True)
        break
