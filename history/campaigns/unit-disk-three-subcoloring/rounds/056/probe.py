import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('p',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
spec=importlib.util.spec_from_file_location('search',r.parent/'053/search.py')
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
algorithm=p.root/'work/algorithm.py'
graphs=p.bases()
for case in json.loads((p.root/'work/cases.json').read_text()):
    if case['name'] in ('positive-unit','opposite-units'):continue
    source=case['source'];name=case['name']
    source_yes=any(all(any(values[abs(v)-1]==(v>0) for v in clause) for clause in source['clauses']) for values in itertools.product((False,True),repeat=source['n']))
    assert source_yes==case['yes']
    with (r/f'{name}-target.json').open('w') as out:
        subprocess.run([sys.executable,str(algorithm)],input=json.dumps(source),stdout=out,text=True,check=True)
    points,scale=p.load_points(r/f'{name}-target.json')
    print(json.dumps({'event':'actual_output','case':name,'vertices':len(points)}),flush=True)
    if name=='empty':
        assert len(points)==0
        w=[]
    else:
        with (r/f'{name}-copies.json').open('w') as out:
            subprocess.run([sys.executable,str(r/'certificate.py')],input=json.dumps(source),stdout=out,text=True,check=True)
        copies=json.loads((r/f'{name}-copies.json').read_text())
        terminal_colors=p.project(points,scale,copies,graphs)
        if not source_yes:
            assert terminal_colors is None
            print(json.dumps({'event':'full_source','case':name,'source':False,'target':False,'recoveries':0}),flush=True)
            continue
        assert terminal_colors is not None
        w=s.search(points,scale,copies,terminal_colors,r/f'{name}-witness.json')
        assert w is not None,'target oracle returned unknown'
    for perm in itertools.permutations(range(3)):
        request={'source':source,'target_solution':[perm[c] for c in w]}
        result=json.loads(subprocess.run([sys.executable,str(algorithm),'--extract'],input=json.dumps(request),capture_output=True,text=True,check=True).stdout)
        assert isinstance(result,dict) and set(result)=={'assignment'}
        assignment=result['assignment']
        assert all(type(v) is bool and k.isdecimal() and k==str(int(k)) and 1<=int(k)<=source['n'] for k,v in assignment.items())
        assert all(any(assignment.get(str(abs(v)),False)==(v>0) for v in clause) for clause in source['clauses'])
    print(json.dumps({'event':'full_source','case':name,'source':True,'target':True,'recoveries':6}),flush=True)
