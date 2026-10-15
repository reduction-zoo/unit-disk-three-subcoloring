import importlib.util
import json
import sys
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('n',r.parent/'051/network.py')
n=importlib.util.module_from_spec(spec);spec.loader.exec_module(n)
spec=importlib.util.spec_from_file_location('emitter',r.parent/'054/certificate_emitter.py')
e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
sys.set_int_max_str_digits(0)
s=json.load(sys.stdin)
copies,count=e.construct(n.construct(s),lambda point:None)
json.dump(copies,sys.stdout)
