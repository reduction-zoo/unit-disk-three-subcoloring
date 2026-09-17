import importlib.util
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('candidate',root/'work/algorithm.py')
candidate=importlib.util.module_from_spec(spec);spec.loader.exec_module(candidate)

routing=json.loads((root/'rounds/032/routing.json').read_text())
positions=sorted({tuple(p) for path in routing['paths'] for p in path['points']});index={p:i for i,p in enumerate(positions)}
net={'points':positions,'segments':[(index[tuple(a)],index[tuple(b)],path['kind'] if k==0 else 'eq') for path in routing['paths'] for k,(a,b) in enumerate(zip(path['points'],path['points'][1:]))]}
assert candidate.target_size(net)==409345
print(json.dumps({'event':'macro_size_check','vertices':409345}),flush=True)
net=json.loads((root/'rounds/038/no-network.json').read_text());rank={p:i for i,p in enumerate(sorted(map(tuple,net['points'])))}
assert [137*rank[tuple(p)] for p in net['points']]==json.loads((root/'rounds/038/ports.json').read_text())
print(json.dumps({'event':'recovery_index_formula','matches_emitted_ports':True}),flush=True)
