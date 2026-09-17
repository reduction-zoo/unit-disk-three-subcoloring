import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'033'))
import geometry as g
r=Path(__file__).parent
routing=json.loads((g.root/'rounds/032/routing.json').read_text())
rows=[json.loads(x) for x in (g.root/'rounds/032/output.jsonl').read_text().splitlines()]


def construct(colors):
    witness=next(x['witness'] for x in rows if x.get('ports')==colors)
    hubs={};segments=[]
    for path in routing['paths']:
        ps=[tuple(g.step*v for v in p) for p in path['points']]
        ca,cb=[witness[v] for v in path['ends']]
        for k,p in enumerate(ps):
            color=ca if k==0 else cb
            if p in hubs:assert hubs[p]==color
            hubs[p]=color
        for k,(a,b) in enumerate(zip(ps,ps[1:])):
            segments.append((a,b,k==0 and path['kind']=='ne',ca if k==0 else cb,cb))
    d=g.Drawing()
    for p,c in sorted(hubs.items()):d.hub(p,c)
    for args in segments:d.segment(*args)
    return d


if __name__=='__main__':
    for colors in ([0,0,0,0],[0,1,0,1]):
        d=construct(colors)
        print(json.dumps({'event':'constructed','ports':colors,'vertices':len(d.points),'copies':len(d.copies)}),flush=True)
        valid,failure,adj=g.validate(d.points,d.colors)
        assert valid,failure
        originals={'eq':g.wire.original,'ne':g.wire.check.graph(g.I)}
        for kind,ids in d.copies:
            assert [[v in adj[u] for v in ids] for u in ids]==originals[kind]
        print(json.dumps({'event':'validated','ports':colors,'valid':valid,'local_copies':len(d.copies)}),flush=True)
        (r/f'witness-{colors[1]}.json').write_text(json.dumps(d.colors))
        if colors[1]==1:(r/'crossover.json').write_text(json.dumps(d.target()))
