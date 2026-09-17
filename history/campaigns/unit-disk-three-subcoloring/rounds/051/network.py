import importlib.util
import json
from pathlib import Path
root=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('sat_source',root/'rounds/028/source.py')
source=importlib.util.module_from_spec(spec);spec.loader.exec_module(source)
routing=json.loads((root/'rounds/032/routing.json').read_text())


def construct(s):
    count,edges=source.construct(s)
    edges=sorted({tuple(sorted(e)) for e in edges})
    incident=[[j for j,e in enumerate(edges) if v in e] for v in range(count)]
    assert all(incident)
    points=[];indices={};segments=[];crossings=0
    def node(p):
        p=tuple(p)
        if p not in indices:indices[p]=len(points);points.append(p)
        return indices[p]
    def segment(a,b,kind):
        segments.append((node(a),node(b),kind))
    for col,(u,v) in enumerate(edges):
        for row in range(count):
            x,y=40*col,40*row
            active=incident[row][0]<=col<=incident[row][-1]
            if u<row<v and active:
                crossings+=1
                for path in routing['paths']:
                    ps=[(x+1+p[0],y+1+p[1]) for p in path['points']]
                    for k,(a,b) in enumerate(zip(ps,ps[1:])):
                        segment(a,b,path['kind'] if k==0 else 'eq')
                segment((x+20,y),(x+20,y+1),'eq')
                segment((x,y+20),(x+1,y+20),'eq')
            else:
                center=(x+20,y+20)
                if active:
                    segment((x,y+20),center,'eq');segment(center,(x+40,y+20),'eq')
                if u<row<v:
                    segment((x+20,y),(x+20,y+40),'eq')
                if row==u:segment(center,(x+20,y+40),'eq')
                if row==v:segment((x+20,y),center,'ne')
    representatives=[indices[40*incident[v][0],40*v+20] for v in range(count)]
    ranks=[{v:i for i,v in enumerate(sorted({p[k] for p in points}))} for k in range(2)]
    points=[[ranks[k][p[k]] for k in range(2)] for p in points]
    return {'points':points,'segments':segments,'representatives':representatives,'crossings':crossings,'source_vertices':count,'source_edges':len(edges)}


def extract(s,network,w):
    return source.extract(s,[w[i] for i in network['representatives']])
