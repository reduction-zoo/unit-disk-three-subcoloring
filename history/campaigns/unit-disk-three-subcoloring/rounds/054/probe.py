import importlib.util
import json
import sys
from pathlib import Path
import certificate_emitter as emitter
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('n',r.parent/'051/network.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
spec=importlib.util.spec_from_file_location('p',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
s=json.loads((r/'source.json').read_text())
assert not any(all(any(value==(v>0) for v in clause) for clause in s['clauses']) for value in (False,True))
copies,count=emitter.construct(n.construct(s),lambda point:None)
(r/'copies.json').write_text(json.dumps(copies))
points,scale=p.load_points(r/'target.json');assert count==len(points)
graphs=p.bases();values=p.project(points,scale,copies,graphs)
assert values is None
print(json.dumps({'event':'full_source_NO','vertices':count,'copies':len(copies),'source_NO':True,'target_NO':True}),flush=True)
