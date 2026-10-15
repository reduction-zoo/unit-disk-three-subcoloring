import itertools
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
t=json.loads((root/'rounds/032/routing.json').read_text())


def cell(kind,offset):
    x,y=offset
    if kind=='cross':
        paths=[[(x+1+p[0],y+1+p[1]) for p in e['points']] for e in t['paths']]
        paths += [[(x+20,y),(x+20,y+1)],[(x,y+20),(x+1,y+20)]]
    else:
        paths=[[(x,y+20),(x+20,y+20)],[(x+20,y+20),(x+40,y+20)]]
        if kind=='lower':paths.append([(x+20,y+20),(x+20,y+40)])
        if kind=='upper':paths.append([(x+20,y),(x+20,y+20)])
    return [(a,b) for ps in paths for a,b in zip(ps,ps[1:])]


count=0
for offset in ((40,0),(0,40),(40,40),(-40,40)):
    for first,second in itertools.product(('cross','lower','upper','bus'),repeat=2):
        segments=cell(first,(0,0))+cell(second,offset);degrees={};occupied={}
        for a,b in segments:
            degrees[a]=degrees.get(a,0)+1;degrees[b]=degrees.get(b,0)+1
            dx=(b[0]>a[0])-(b[0]<a[0]);dy=(b[1]>a[1])-(b[1]<a[1])
            for k in range(abs(a[0]-b[0])+abs(a[1]-b[1])+1):
                p=(a[0]+k*dx,a[1]+k*dy)
                for c,d in occupied.get(p,()):assert p in (a,b) and p in (c,d)
                occupied.setdefault(p,[]).append((a,b))
        assert max(degrees.values())<=4
        count+=1
print(json.dumps({'adjacent_or_diagonal_type_pairs':count,'noncrossing':True,'maximum_degree':4}))
