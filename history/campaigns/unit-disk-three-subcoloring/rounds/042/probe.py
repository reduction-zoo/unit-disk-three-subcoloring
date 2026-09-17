import importlib.util
import itertools
import json
from pathlib import Path
r=Path(__file__).parent
# Load only definitions: the older module has a top-level experiment.
scope={"__file__":str(r.parent/'024/probe.py')}
exec((r.parent/'024/probe.py').read_text().split("for x,y in itertools.product")[0],scope)
for x,y,i,j in itertools.product(range(50,54),range(50,54),(0,1,4,5),(0,1,4,5)):
    local,clean=scope['pair'](i,j,x*scope['q'],y*scope['q'])
    print(json.dumps({'lengths':[x,y],'states':[i,j],'local':local,'clean':clean}),flush=True)
