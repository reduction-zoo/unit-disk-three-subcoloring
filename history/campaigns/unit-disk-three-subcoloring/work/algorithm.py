import importlib.util
import json
import sys
from pathlib import Path
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('source_network',root/'rounds/051/network.py')
network=importlib.util.module_from_spec(spec);spec.loader.exec_module(network)
spec=importlib.util.spec_from_file_location('coordinate_map',root/'rounds/051/geometry.py')
geometry=importlib.util.module_from_spec(spec);spec.loader.exec_module(geometry)


def valid_source(s):
    return (isinstance(s,dict) and set(s)=={'n','clauses'} and type(s['n']) is int and s['n']>=0 and isinstance(s['clauses'],list) and all(isinstance(c,list) and len(c)==3 and all(type(v) is int and 1<=abs(v)<=s['n'] for v in c) for c in s['clauses']))


def target_size(net):
    length=sum(abs(net['points'][a][0]-net['points'][b][0])+abs(net['points'][a][1]-net['points'][b][1]) for a,b,k in net['segments'])
    return 137*len(net['points'])+238*length-69*len(net['segments'])


def forward(s):
    if not valid_source(s):
        print('null');return
    if not s['clauses']:
        print('{"centers":[]}');return
    net=network.construct(s)
    sys.stdout.write('{"centers":[');first=True
    def emit(p):
        nonlocal first
        if not first:sys.stdout.write(',')
        first=False
        sys.stdout.write(json.dumps([[v.numerator,v.denominator] for v in p],separators=(',',':')))
    _,count=geometry.construct(net,emit)
    assert count==target_size(net)
    sys.stdout.write(']}\n')


def extract(s,w):
    if not valid_source(s):raise ValueError('invalid source')
    if not s['clauses']:
        if w!=[]:raise ValueError('invalid empty target witness')
        return {'assignment':{}}
    net=network.construct(s)
    if not isinstance(w,list) or len(w)!=target_size(net) or any(type(c) is not int or not 0<=c<3 for c in w):raise ValueError('invalid target witness encoding')
    rank={p:i for i,p in enumerate(sorted(map(tuple,net['points'])))}
    colors=[w[137*rank[tuple(net['points'][v])]] for v in net['representatives']]
    return network.source.extract(s,colors)


if __name__=='__main__':
    if sys.argv[1:]==['--extract']:
        request=json.load(sys.stdin);print(json.dumps(extract(request['source'],request['target_solution'])))
    elif not sys.argv[1:]:
        try:source=json.load(sys.stdin)
        except (json.JSONDecodeError,RecursionError):source=None
        forward(source)
    else:raise ValueError('unknown command arguments')
