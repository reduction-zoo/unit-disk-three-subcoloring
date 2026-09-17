import importlib.util
import json
import subprocess
import sys
from pathlib import Path
r=Path(__file__).parent;root=r.parents[1]
spec=importlib.util.spec_from_file_location('candidate',root/'work/algorithm.py');candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate)
sys.path.insert(0,str(root/'work'));import check
for s in ({'n':0,'clauses':[]},{'n':10**5000,'clauses':[]}):
    t=json.loads(subprocess.run([sys.executable,str(root/'work/algorithm.py')],input=json.dumps(s),text=True,capture_output=True,check=True).stdout)
    w=check.solve_coloring(check.graph(t));assert w is not None and check.source_solve(s) is not None
    recovered=json.loads(subprocess.run([sys.executable,str(root/'work/algorithm.py'),'--extract'],input=json.dumps({'source':s,'target_solution':w}),text=True,capture_output=True,check=True).stdout)
    assert check.source_witness(s,recovered)
    print(json.dumps({'event':'full_empty_source','source_bytes':len(json.dumps(s)),'target_vertices':len(t['centers']),'recovered_bytes':len(json.dumps(recovered))}),flush=True)
for raw in ('{','null','[]','{"n":true,"clauses":[]}','{"n":1,"clauses":[[0,1,1]]}','{"n":1,"clauses":[[2,2,2]]}'):
    out=subprocess.run([sys.executable,str(root/'work/algorithm.py')],input=raw,text=True,capture_output=True,check=True).stdout
    assert json.loads(out) is None
print(json.dumps({'event':'malformed_rejected','count':6}),flush=True)
for name,expected in [('rounds/038/no-network.json',4250)]:
    net=json.loads((root/name).read_text());assert candidate.target_size(net)==expected
print(json.dumps({'event':'rectangle_size_check','vertices':4250}),flush=True)
for case in json.loads((root/'work/cases.json').read_text()):
    s=case['source'];net=candidate.network.construct(s)
    count=candidate.target_size(net) if s['clauses'] else 0
    print(json.dumps({'event':'projected_full_target','case':case['name'],'vertices':count,'constructed':not bool(s['clauses'])}),flush=True)
