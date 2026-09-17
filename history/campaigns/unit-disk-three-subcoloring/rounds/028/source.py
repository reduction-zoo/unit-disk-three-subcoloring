import json
from pathlib import Path
G=json.loads((Path(__file__).resolve().parents[1]/'027/gadgets.json').read_text())


def construct(s):
    labels=sorted({abs(v) for c in s['clauses'] for v in c})
    index={v:i for i,v in enumerate(labels)}
    edges=[(0,1),(1,2),(0,2)]
    for i in range(len(labels)):
        a=3+2*i;b=a+1
        edges.extend([(a,b),(a,2),(b,2)])
    count=3+2*len(labels)
    for clause in s['clauses']:
        ids=[3+2*index[abs(v)]+(v<0) for v in clause]+list(range(count,count+6))
        edges.extend((ids[a],ids[b]) for a,b in G['clause_edges'])
        edges.extend([(count+5,1),(count+5,2)])
        count+=6
    return count,edges


def extract(s,w):
    labels=sorted({abs(v) for c in s['clauses'] for v in c})
    return {'assignment':{str(v):w[3+2*i]==w[0] for i,v in enumerate(labels)}}
