import importlib.util
import itertools
import json
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('connector',r.parent/'025/probe.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)
for x,y in itertools.product(range(50,54),repeat=2):
    c.L=x*c.q;c.R=y*c.q
    t,w,valid=c.connector((False,False),1,0)
    print(json.dumps({'lengths':[x,y],'valid':valid}),flush=True)
