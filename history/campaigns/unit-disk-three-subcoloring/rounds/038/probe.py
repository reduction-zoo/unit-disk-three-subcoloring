import json
from pathlib import Path
import geometry
r=Path(__file__).parent
routing=json.loads((geometry.root/'rounds/032/routing.json').read_text())
positions=sorted({tuple(p) for path in routing['paths'] for p in path['points']});index={p:i for i,p in enumerate(positions)}
net={'points':positions,'segments':[(index[tuple(a)],index[tuple(b)],path['kind'] if k==0 else 'eq') for path in routing['paths'] for k,(a,b) in enumerate(zip(path['points'],path['points'][1:]))]}
expected=json.loads((geometry.root/'rounds/034/crossover.json').read_text())['centers']
cursor=0

def compare(p):
    global cursor
    assert [[v.numerator,v.denominator] for v in p]==expected[cursor]
    cursor+=1

ports,n=geometry.construct(net,compare)
assert cursor==n==len(expected)
print(json.dumps({'event':'same_coordinates','vertices':n,'all_equal':True}),flush=True)
net={'points':[(0,0),(1,0),(1,1),(0,1)],'segments':[(0,1,'eq'),(1,2,'eq'),(2,3,'eq'),(3,0,'ne')]}
points=[];ports,n=geometry.construct(net,points.append)
(r/'no-network.json').write_text(json.dumps(net));(r/'no-target.json').write_text(json.dumps({'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}));(r/'ports.json').write_text(json.dumps(ports))
print(json.dumps({'event':'uncolorable_network_constructed','vertices':n,'ports':ports}),flush=True)
