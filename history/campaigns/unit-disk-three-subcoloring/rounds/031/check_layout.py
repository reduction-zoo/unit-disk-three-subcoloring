import itertools
import json
from pathlib import Path
r=Path(__file__).parent
data=json.loads((r/'layout.json').read_text())
centers={v['_gvid']:tuple(10*round(float(t)/10) for t in v['pos'].split(',')) for v in data['objects']}
paths=[]
for edge in data['edges']:
    points=[centers[edge['tail']]]+[tuple(10*round(float(x)/10) for x in p.split(',')) for p in edge['pos'].split()]+[centers[edge['head']]]
    clean=[]
    for p in points:
        if not clean or p!=clean[-1]:clean.append(p)
    paths.append({'ends':[edge['tail'],edge['head']],'points':clean})
segments=[(i,a,b) for i,e in enumerate(paths) for a,b in zip(e['points'],e['points'][1:])]
nonorth=[(i,a,b) for i,a,b in segments if a[0]!=b[0] and a[1]!=b[1]]
conflicts=[]
for (i,a,b),(j,c,d) in itertools.combinations(segments,2):
    if i==j:continue
    lo=[max(min(a[k],b[k]),min(c[k],d[k])) for k in range(2)]
    hi=[min(max(a[k],b[k]),max(c[k],d[k])) for k in range(2)]
    if any(lo[k]>hi[k] for k in range(2)):continue
    common=set(paths[i]['ends'])&set(paths[j]['ends'])
    if lo==hi and tuple(lo) in [centers[v] for v in common]:continue
    conflicts.append({'edges':[i,j],'overlap':[lo,hi]})
(r/'paths.json').write_text(json.dumps(paths))
print(json.dumps({'paths':len(paths),'segments':len(segments),'nonorthogonal':nonorth,'conflicts':conflicts}))
