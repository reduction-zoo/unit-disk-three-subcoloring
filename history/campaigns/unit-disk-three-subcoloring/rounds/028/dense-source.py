import json
from pathlib import Path
G=json.loads((Path(__file__).resolve().parents[1]/'027/gadgets.json').read_text())


def construct(s):
    edges=[(0,1),(1,2),(0,2)]
    for i in range(s['n']):
        a=3+2*i;b=a+1
        edges.extend([(a,b),(a,2),(b,2)])
    count=3+2*s['n']
    for clause in s['clauses']:
        ids=[3+2*(abs(v)-1)+(v<0) for v in clause]+list(range(count,count+6))
        edges.extend((ids[a],ids[b]) for a,b in G['clause_edges'])
        edges.extend([(count+5,1),(count+5,2)])
        count+=6
    return count,edges


def extract(s,w):
    return [w[3+2*i]==w[0] for i in range(s['n'])]
