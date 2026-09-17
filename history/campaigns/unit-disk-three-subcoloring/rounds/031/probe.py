import json
import math
import subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[2]
g=json.loads((root/'rounds/027/gadgets.json').read_text())
xy=g['cross_coords'];edges=g['cross_edges'];neighbors=[[] for p in xy]
for a,b in edges:neighbors[a].append(b);neighbors[b].append(a)
points=[];ids={};mixed=[];representatives=[]
for v,(x,y) in enumerate(xy):
    ns=sorted(neighbors[v],key=lambda u:math.atan2(xy[u][1]-y,xy[u][0]-x))
    if len(ns)<=4:
        k=len(points);points.append((x*400,y*400));representatives.append(k)
        for u in ns:ids[v,u]=k
    else:
        cycle=[]
        for u in ns:
            dx=xy[u][0]-x;dy=xy[u][1]-y;d=max(abs(dx),abs(dy))
            k=len(points);points.append((x*400+80*dx/d,y*400+80*dy/d));ids[v,u]=k;cycle.append(k)
        representatives.append(cycle[0])
        mixed.extend((a,b,'eq') for a,b in zip(cycle,cycle[1:]+cycle[:1]))
mixed.extend((ids[a,b],ids[b,a],'ne') for a,b in edges)
lines=['graph G { graph [splines=ortho, overlap=true]; node [shape=point,width=0.05,height=0.05];']
lines += [f'{i} [pos="{x},{y}!"];' for i,(x,y) in enumerate(points)]
lines += [f'{a} -- {b};' for a,b,kind in mixed]+['}']
r=Path(__file__).parent
(r/'layout.dot').write_text('\n'.join(lines))
result=subprocess.run(['neato','-n2','-Tjson',str(r/'layout.dot')],capture_output=True,text=True,check=True)
(r/'layout.json').write_text(result.stdout);(r/'stderr.txt').write_text(result.stderr)
(r/'network.json').write_text(json.dumps({'points':points,'edges':mixed,'representatives':representatives,'ports':[representatives[i] for i in (9,10,11,12)]}))
print(json.dumps({'vertices':len(points),'edges':len(mixed),'max_degree':max(sum(a==i or b==i for a,b,k in mixed) for i in range(len(points)))}))
