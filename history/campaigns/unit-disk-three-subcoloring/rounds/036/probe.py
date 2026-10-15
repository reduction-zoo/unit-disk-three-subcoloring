import itertools
import json
import sys
from pathlib import Path
import network
sys.path.insert(0,str(network.root/'work'))
import check
import z3
r=Path(__file__).parent
for case in json.loads((network.root/'work/cases.json').read_text()):
    s=case['source'];net=network.construct(s)
    c=[z3.Int(f'c{i}') for i in range(len(net['points']))];q=z3.Solver()
    q.add(*[z3.And(v>=0,v<3) for v in c])
    for a,b,kind in net['segments']:q.add(c[a]==c[b] if kind=='eq' else c[a]!=c[b])
    result=q.check();assert result in (z3.sat,z3.unsat)
    assert (result==z3.sat)==case['yes']==(check.source_solve(s) is not None)
    recovered=0
    if result==z3.sat:
        w=[q.model().eval(v).as_long() for v in c]
        for perm in itertools.permutations(range(3)):
            assert check.source_witness(s,network.extract(s,net,[perm[v] for v in w]));recovered+=1
        (r/(case['name']+'-witness.json')).write_text(json.dumps(w))
    (r/(case['name']+'-network.json')).write_text(json.dumps(net))
    print(json.dumps({'case':case['name'],'status':str(result),'vertices':len(c),'segments':len(net['segments']),'crossings':net['crossings'],'intermediate_recoveries':recovered}),flush=True)
