import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('g',r.parent/'048/geometry.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
spec=importlib.util.spec_from_file_location('n',r/'network.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
s=json.loads((r/'source.json').read_text());net=n.construct(s)
w=json.loads((r.parent/'045/positive-unit-witness.json').read_text())
d=g.Drawing()
for index in sorted(range(len(net['points'])),key=lambda i:net['points'][i]):
    d.hub(tuple(g.step*v for v in net['points'][index]),w[index])
for a,b,kind in net['segments']:
    d.segment(tuple(g.step*v for v in net['points'][a]),tuple(g.step*v for v in net['points'][b]),kind=='ne',w[a],w[b])
print(json.dumps({'event':'fixture','vertices':len(d.points),'copies':len(d.copies)}),flush=True)
t=json.loads((r/'target.json').read_text())
assert len(t['centers'])==len(d.points)
for expected,actual in zip(d.points,t['centers']):
    assert all(v.numerator==pair[0] and v.denominator==pair[1] for v,pair in zip(expected,actual))
del t
valid,failure,adj=g.validate(d.points,d.colors)
assert valid, failure
del adj
(r/'witness.json').write_text(json.dumps(d.colors))
(r/'copies.json').write_text(json.dumps(d.copies))
print(json.dumps({'event':'actual_full_target_witness','vertices':len(d.points),'valid':valid,'independent_target_solve':False}),flush=True)
for perm in itertools.permutations(range(3)):
    request={'source':s,'target_solution':[perm[c] for c in d.colors]}
    result=json.loads(subprocess.run([sys.executable,str(n.root/'work/algorithm.py'),'--extract'],input=json.dumps(request),capture_output=True,text=True,check=True).stdout)
    assert g.wire.check.source_witness(s,result)
    print(json.dumps({'event':'recovery','permutation':perm,'assignment':result}),flush=True)
