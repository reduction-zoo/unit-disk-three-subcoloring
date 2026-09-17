from fractions import Fraction
from itertools import combinations,product
import json,sys,re
sys.set_int_max_str_digits(0)


def construct(source):
    n,clauses=source['n'],source['clauses']
    if type(n) is not int or n<0 or not isinstance(clauses,list):raise ValueError('Invalid 3SAT instance')
    if any(not isinstance(c,list) or len(c)!=3 or any(type(l) is not int or not 1<=abs(l)<=n for l in c) for c in clauses):raise ValueError('Invalid clause')
    fresh=n;normalized=[]
    for clause in clauses:
        c=list(dict.fromkeys(clause))
        if any(-l in c for l in c):continue
        if len(c)==3:normalized.append(c)
        elif len(c)==2:
            fresh+=1;normalized.extend([c+[fresh],c+[-fresh]])
        else:
            a,b=fresh+1,fresh+2;fresh+=2
            normalized.extend([c+[sa*a,sb*b] for sa,sb in product((-1,1),repeat=2)])
    triples=[];occurrences={};labels=[]
    for c in normalized:
        for _ in range(2):
            triple=[]
            for literal in c:
                i=len(labels);labels.append(literal);triple.append(i)
                occurrences.setdefault(abs(literal),[]).append(i)
            triples.append(triple)
    k=len(labels);edges=[];black=[]
    for i in range(k):
        a=5*i;black.extend((a,a+1))
        edges.extend((a+b,a+w) for b in (0,1) for w in (2,3,4));edges.append((a+2,a+3))
    for c in triples:edges.extend(combinations([5*i+2 for i in c],2))
    vertices=5*k
    for indices in occurrences.values():
        for i,j in zip(indices,indices[1:]+indices[:1]):
            u=5*i+(4 if labels[i]>0 else 3)
            v=5*j+(3 if labels[j]>0 else 4)
            l,p=vertices,vertices+1;vertices+=2;black.extend((l,p))
            edges.extend(((u,v),(u,l),(v,l),(l,p)))
    core_n=vertices;core_edges=list(edges)
    for v in black:
        a,b=vertices,vertices+4;vertices+=8
        edges.extend(((v,a),(v,b),(a,b)))
        edges.extend((a,a+i) for i in (1,2,3));edges.extend((b,b+i) for i in (1,2,3))
    graph={'n':vertices,'edges':sorted([sorted(e) for e in edges])}
    return graph,core_n,core_edges,black,labels,occurrences


def extract(source,witness):
    graph,core_n,core_edges,black,labels,occurrences=construct(source)
    if any(not isinstance(a,str) or re.fullmatch(r'-?[0-9]+(?:/[1-9][0-9]*)?',a) is None for row in witness['left'] for a in row):raise ValueError('Expected explicitly encoded integer or rational endpoints')
    left=[[Fraction(a) for a in row] for row in witness['left']]
    if len(left)!=graph['n'] or any(len(row)!=2 for row in left):raise ValueError('Invalid witness shape')
    neighbors=[[] for _ in range(core_n)]
    for u,v in core_edges:neighbors[u].append(v);neighbors[v].append(u)
    core=[list(row) for row in left[:core_n]]
    for v in black:
        active=[a for a in left[v] if any(abs(a-b)<1 for u in neighbors[v] for b in left[u])]
        if len(active)!=1:raise ValueError('Black vertex does not have one active component')
        core[v]=active
    values=[]
    for i in range(len(labels)):
        a=5*i
        free=any(all(abs(x-y)>=1 for row in core[a:a+2] for y in row) for row in core[a+2:a+4] for x in row)
        values.append(free)
    assignment={}
    for variable,indices in occurrences.items():
        if variable<=source['n']:
            i=indices[0];assignment[str(variable)]=values[i] if labels[i]>0 else not values[i]
    return {'assignment':assignment}


if __name__=='__main__':
    data=json.load(sys.stdin)
    if sys.argv[1:]==['--extract']:result=extract(data['source'],data['target_solution'])
    elif not sys.argv[1:]:result=construct(data)[0]
    else:raise ValueError('Expected no argument or --extract')
    print(json.dumps(result))
