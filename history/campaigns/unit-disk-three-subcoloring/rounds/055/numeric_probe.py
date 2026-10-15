import importlib.util
import json
from pathlib import Path
r=Path(__file__).parent
spec=importlib.util.spec_from_file_location('p',r.parent/'052/project.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
for value in (-(2**63),-(2**51),2**51,2**51-1):
    file=r/'numeric-bound.json';file.write_text(json.dumps({'centers':[[[value,1],[0,1]]]}))
    try:p.load_points(file);accepted=True
    except AssertionError:accepted=False
    assert accepted==(abs(value)<2**51)
    print(json.dumps({'coordinate':value,'accepted':accepted}))
