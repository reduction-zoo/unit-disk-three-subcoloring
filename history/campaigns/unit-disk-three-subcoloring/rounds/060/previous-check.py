import argparse
import itertools
import json
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
import z3
sys.set_int_max_str_digits(0)


def source_valid(s):
    return (isinstance(s, dict) and set(s) == {'n', 'clauses'}
            and type(s['n']) is int and s['n'] >= 0
            and isinstance(s['clauses'], list)
            and all(isinstance(c, list) and len(c) == 3
                    and all(type(v) is int and 1 <= abs(v) <= s['n'] for v in c)
                    for c in s['clauses']))


def source_witness(s, w):
    if not source_valid(s) or not isinstance(w,dict) or set(w)!={'assignment'} or not isinstance(w['assignment'],dict):
        return False
    values=w['assignment']
    if any(not isinstance(k,str) or not k.isascii() or not k.isdecimal() or k!=str(int(k)) or not 1<=int(k)<=s['n'] or type(v) is not bool for k,v in values.items()):
        return False
    return all(any(values.get(str(abs(v)),False)==(v>0) for v in c) for c in s['clauses'])


def source_solve(s):
    if not source_valid(s):
        return None
    labels=sorted({abs(v) for c in s['clauses'] for v in c})
    vs={i:z3.Bool(f'b{i}') for i in labels}
    q=z3.Solver()
    for c in s['clauses']:
        q.add(z3.Or([vs[abs(v)] if v>0 else z3.Not(vs[abs(v)]) for v in c]))
    status=q.check()
    if status==z3.unsat:
        return None
    if status!=z3.sat:
        raise RuntimeError(str(status))
    w={'assignment':{str(i):z3.is_true(q.model().eval(v,model_completion=True)) for i,v in vs.items()}}
    assert source_witness(s,w)
    return w


def centers(t):
    if not isinstance(t, dict) or set(t) != {'centers'} or not isinstance(t['centers'], list):
        raise ValueError('invalid target')
    out = []
    for pair in t['centers']:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError('invalid center')
        xy = []
        for v in pair:
            if (not isinstance(v, list) or len(v) != 2
                    or any(type(a) is not int for a in v) or v[1] <= 0):
                raise ValueError('invalid rational')
            xy.append(Fraction(*v))
        out.append(xy)
    return out


def graph(t):
    ps = centers(t)
    return [[i != j and sum((a-b)**2 for a, b in zip(ps[i], ps[j])) <= 1
             for j in range(len(ps))] for i in range(len(ps))]


def paths(adj):
    return [v for v in itertools.combinations(range(len(adj)), 3)
            if sum(adj[i][j] for i, j in itertools.combinations(v, 2)) == 2]


def valid_coloring(adj, w, k=3):
    if not isinstance(w, list) or len(w) != len(adj) or any(type(c) is not int or not 0 <= c < k for c in w):
        return False
    # Check connected monochromatic components are cliques, independently of P3 encoding.
    unseen = set(range(len(adj)))
    while unseen:
        root = unseen.pop()
        component, todo = {root}, [root]
        while todo:
            i = todo.pop()
            ns = {j for j in unseen if adj[i][j] and w[i] == w[j]}
            unseen -= ns
            component |= ns
            todo.extend(ns)
        if any(not adj[i][j] for i, j in itertools.combinations(component, 2)):
            return False
    return True


def color_solver(adj, k=3):
    vs = [z3.Int(f'c{i}') for i in range(len(adj))]
    q = z3.Solver()
    q.add([z3.And(v >= 0, v < k) for v in vs])
    for a, b, c in paths(adj):
        q.add(z3.Or(vs[a] != vs[b], vs[b] != vs[c]))
    return q, vs


def solve_coloring(adj, k=3):
    q, vs = color_solver(adj, k)
    status = q.check()
    if status == z3.unsat:
        return None
    if status != z3.sat:
        raise RuntimeError(str(status))
    w = [q.model().eval(v).as_long() for v in vs]
    assert valid_coloring(adj, w, k)
    return w


def target_witness(t, w):
    return valid_coloring(graph(t), w)


def check_pair(s, t, w):
    adj = graph(t)
    actual = solve_coloring(adj)
    if (source_solve(s) is None) != (actual is None):
        raise AssertionError('decision mismatch')
    if actual is not None and not source_witness(s, w):
        raise AssertionError('invalid recovery')


def self_test():
    count = 0
    for n in range(5):
        edges = list(itertools.combinations(range(n), 2))
        for mask in range(1 << len(edges)):
            adj = [[False]*n for _ in range(n)]
            for bit, (i, j) in enumerate(edges):
                adj[i][j] = adj[j][i] = bool(mask >> bit & 1)
            for k in (1, 2, 3):
                brute = any(valid_coloring(adj, list(w), k) for w in itertools.product(range(k), repeat=n))
                assert (solve_coloring(adj, k) is not None) == brute
                count += 1
    cases = json.loads(Path(__file__).with_name('cases.json').read_text())
    for case in cases:
        s = case['source']
        brute = any(source_witness(s, {'assignment':{str(i+1):v for i,v in enumerate(w)}}) for w in itertools.product((False, True), repeat=s['n']))
        assert brute == case['yes'] == (source_solve(s) is not None)
    # Binary recursive cone: chi_s increases by one at each step; BC4 needs four colors.
    adj = [[False]]
    for _ in range(3):
        n = len(adj)
        adj = [[(i == 2*n or j == 2*n) if i != j and (i == 2*n or j == 2*n)
                else (adj[i % n][j % n] if i < 2*n and j < 2*n and i//n == j//n else False)
                for j in range(2*n+1)] for i in range(2*n+1)]
    assert solve_coloring(adj, 3) is None
    assert solve_coloring(adj, 4) is not None
    p3 = {'centers': [[[0,1],[0,1]], [[1,1],[0,1]], [[2,1],[0,1]]]}
    assert graph(p3) == [[False,True,False],[True,False,True],[False,True,False]]
    assert not target_witness(p3, [0,0,0])
    assert target_witness(p3, [0,0,1])
    for bad in ({}, {'centers': [[[0,0],[0,1]]]}, {'centers': [[[0.0,1],[0,1]]]}):
        try:
            centers(bad)
        except ValueError:
            pass
        else:
            raise AssertionError('malformed target accepted')
    for s, t, w in [(cases[2]['source'], {'centers': []}, []), (cases[1]['source'], p3, [False])]:
        try:
            check_pair(s, t, w)
        except AssertionError:
            pass
        else:
            raise AssertionError('bad rule accepted')
    critical = json.loads((Path(__file__).resolve().parents[1] / 'rounds/008/critical.json').read_text())
    critical_adj = graph(critical)
    assert solve_coloring(critical_adj, 3) is None
    assert solve_coloring(critical_adj, 4) is not None
    print(json.dumps({'z3': z3.get_version_string(), 'graph_oracle_comparisons': count,
                      'source_cases': len(cases), 'abstract_NO_BC4': True,
                      'geometric_NO_fixture': '34-vertex critical grid subgraph', 'malformed_rejected': 3,
                      'bad_rule_rejected': 2}))


def candidate(path, name=None):
    cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    if name is not None:
        cases=[case for case in cases if case['name']==name]
        if not cases:raise ValueError('unknown prepared case')
    for case in cases:
        s = case['source']
        t = json.loads(subprocess.run([sys.executable, path], input=json.dumps(s), capture_output=True, text=True, check=True).stdout)
        adj = graph(t)
        q, vs = color_solver(adj)
        found = 0
        while found < (3**len(adj) if len(adj) <= 6 else 6):
            status = q.check()
            if status == z3.unsat:
                break
            if status != z3.sat:
                raise RuntimeError(str(status))
            w = [q.model().eval(v).as_long() for v in vs]
            assert valid_coloring(adj, w)
            assert case['yes'], 'decision mismatch'
            recovered = json.loads(subprocess.run([sys.executable, path, '--extract'], input=json.dumps({'source':s,'target_solution':w}), capture_output=True, text=True, check=True).stdout)
            assert source_witness(s, recovered), 'invalid recovery'
            found += 1
            q.add(z3.Or([v != c for v,c in zip(vs,w)]))
        assert bool(found) == case['yes'], 'decision mismatch'
        print(json.dumps({'case':case['name'], 'vertices':len(adj), 'recoveries':found}))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--self-test', action='store_true')
    group.add_argument('--candidate')
    parser.add_argument('--case')
    args = parser.parse_args()
    if args.self_test:
        self_test()
    else:
        candidate(args.candidate, args.case)
