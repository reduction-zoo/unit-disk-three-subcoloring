from fractions import Fraction
Q=Fraction
from itertools import combinations,product
import networkx as nx
import z3


def unit_order(graph):
    order=sorted(graph)
    for _ in range(3):
        rank={u:i for i,u in enumerate(order)};labels={u:[] for u in graph};order=[]
        while labels:
            u=max(labels,key=lambda v:(labels[v],rank[v]));del labels[u];order.append(u)
            for v in graph[u]:
                if v in labels:labels[v].append(len(graph)-len(order))
    position={u:i for i,u in enumerate(order)}
    for u in graph:
        closed=[position[v] for v in [u,*graph[u]]]
        if max(closed)-min(closed)+1!=len(closed):return None
    return order


def solve(adj,counts):
    groups=[];owner=[]
    for u,c in enumerate(counts):
        groups.append(list(range(len(owner),len(owner)+c)));owner.extend([u]*c)
    possible=nx.Graph();possible.add_nodes_from(range(len(owner)))
    relation={};solver=z3.Solver()
    for u,row in enumerate(adj):
        for v in sorted(row):
            if v<=u:continue
            edge=[]
            for a,b in product(groups[u],groups[v]):
                key=tuple(sorted((a,b)));relation[key]=z3.Bool(f'e{key[0]}_{key[1]}');edge.append(relation[key]);possible.add_edge(*key)
            solver.add(z3.Or(*edge))
    def r(a,b):return relation.get(tuple(sorted((a,b))),z3.BoolVal(False))
    for u in possible:
        for a,b,c in combinations(possible[u],3):
            solver.add(z3.Or(z3.Not(r(u,a)),z3.Not(r(u,b)),z3.Not(r(u,c)),r(a,b),r(a,c),r(b,c)))
    for u in possible:
        for v in possible[u]:
            if v<=u:continue
            for w in possible[v]:
                if w<=u or w==v:continue
                for t in set(possible[w])&set(possible[u]):
                    if t<=v or t==w:continue
                    solver.add(z3.Or(z3.Not(r(u,v)),z3.Not(r(v,w)),z3.Not(r(w,t)),z3.Not(r(t,u)),r(u,w),r(v,t)))
    triangles=[]
    for u in possible:
        for v in possible[u]:
            if v<=u:continue
            for w in set(possible[u])&set(possible[v]):
                if w>v:triangles.append((u,v,w))
    for u,v,w in triangles:
        for a,b,c in product(possible[u],possible[v],possible[w]):
            nodes=(u,v,w,a,b,c)
            if len(set(nodes))!=6:continue
            required={tuple(sorted(e)) for e in ((u,v),(v,w),(u,w),(u,a),(v,b),(w,c))}
            absent=[e for e in combinations(sorted(nodes),2) if e not in required]
            solver.add(z3.Or(*[z3.Not(r(*e)) for e in required],*[r(*e) for e in absent]))
    for clique in nx.enumerate_all_cliques(possible):
        if len(clique)>4:break
        if len(clique)==4:solver.add(z3.Or(*[z3.Not(r(a,b)) for a,b in combinations(clique,2)]))
    for attempt in range(1,65):
        verdict=solver.check()
        if verdict==z3.unknown:raise RuntimeError(solver.reason_unknown())
        if verdict==z3.unsat:return False,None,attempt
        model=solver.model();graph=nx.Graph();graph.add_nodes_from(possible)
        graph.add_edges_from(e for e,b in relation.items() if z3.is_true(model.eval(b)))
        coordinate={};offset=Fraction(0);bad=False
        for component in nx.connected_components(graph):
            nodes=unit_order(graph.subgraph(component))
            if nodes is None:
                literals=[z3.Not(b) if graph.has_edge(*e) else b for e,b in relation.items() if set(e)<=component]
                solver.add(z3.Or(*literals));bad=True;break
            linear=z3.SolverFor('QF_LRA');x={u:z3.Real(f'x{u}') for u in nodes}
            linear.add(x[nodes[0]]==0)
            linear.add(*[x[u]<=x[v] for u,v in zip(nodes,nodes[1:])])
            for u,v in combinations(nodes,2):
                linear.add(x[v]-x[u]<1 if graph.has_edge(u,v) else x[v]-x[u]>=1)
            result=linear.check()
            if result==z3.unknown:raise RuntimeError(linear.reason_unknown())
            if result==z3.unsat:
                literals=[z3.Not(b) if graph.has_edge(*e) else b for e,b in relation.items() if set(e)<=component]
                solver.add(z3.Or(*literals));bad=True;break
            witness=linear.model();local={u:witness.eval(x[u],model_completion=True).as_fraction() for u in nodes}
            low=min(local.values());coordinate.update({u:offset+a-low for u,a in local.items()});offset+=max(local.values())-low+2
        if not bad:
            return True,[[coordinate[a] for a in group] for group in groups],attempt
    raise RuntimeError('The declared budget of 64 split candidates was exhausted')

def target(g):
    n=g['n'];adj=[set() for _ in range(n)]
    for u,v in g['edges']:adj[u].add(v);adj[v].add(u)
    gadgets=[];removed=set();black=set()
    for a in range(n):
        leaves=sorted(u for u in adj[a] if len(adj[u])==1)
        if len(adj[a])!=5 or len(leaves)!=3:continue
        for b in sorted(adj[a]):
            if b<=a:continue
            other=sorted(u for u in adj[b] if len(adj[u])==1)
            if len(adj[b])!=5 or len(other)!=3:continue
            common=adj[a]&adj[b]
            if len(common)!=1:continue
            v=next(iter(common));private={a,b,*leaves,*other}
            assert len(private)==8
            if private&(removed|black) or v in removed|black:continue
            assert adj[a]=={v,b,*leaves} and adj[b]=={v,a,*other}
            removed.update(private);black.add(v);gadgets.append((v,a,b,leaves,other))
    kept=sorted(set(range(n))-removed)
    index={u:i for i,u in enumerate(kept)}
    core_adj=[{index[v] for v in adj[u] if v in index} for u in kept]
    yes,core_rows,attempts=solve(core_adj,[1 if u in black else 2 for u in kept])
    if not yes:return False,None,len(gadgets)
    rows=[[] for _ in range(n)]
    for u,row in zip(kept,core_rows):rows[u]=row
    offset=max(sum(rows,[]),default=Q(0))+10
    for v,a,b,aa,bb in gadgets:
        rows[v].append(offset+Q(2,5))
        rows[a]=[offset,offset+5];rows[b]=[offset+Q(4,5),offset+9]
        for u,x,y in zip(aa,[Q(-4,5),Q(21,5),Q(29,5)],[20,24,26]):rows[u]=[offset+x,offset+y]
        for u,x,y in zip(bb,[Q(8,5),Q(41,5),Q(49,5)],[22,28,30]):rows[u]=[offset+x,offset+y]
        offset+=40
    w={'left':[[str(x) for x in row] for row in rows]}
    return True,w,len(gadgets)

