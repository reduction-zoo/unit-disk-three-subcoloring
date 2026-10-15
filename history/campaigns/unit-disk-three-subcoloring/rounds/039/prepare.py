import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'038'))
import geometry
r=Path(__file__).parent
net=json.loads((geometry.root/'rounds/038/no-network.json').read_text());net['segments']=[(a,b,'eq') for a,b,k in net['segments']]
points=[];ports,n=geometry.construct(net,points.append)
(r/'yes-target.json').write_text(json.dumps({'centers':[[[v.numerator,v.denominator] for v in p] for p in points]}));(r/'yes-ports.json').write_text(json.dumps(ports))
print(json.dumps({'vertices':n,'ports':ports}))
