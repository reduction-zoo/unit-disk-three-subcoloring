import json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[2]
out=Path(__file__).parent

def svg(name,width,height,items):
    (out/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'+''.join(items)+'</svg>')
def line(a,b,color='#aaa',dash=''):
    return f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="1" stroke-dasharray="{dash}"/>'
def circle(p,r=3,fill='#333'):
    return f'<circle cx="{p[0]}" cy="{p[1]}" r="{r}" fill="{fill}" stroke="#222"/>'
def text(p,label,size=14):
    return f'<text x="{p[0]}" y="{p[1]}" text-anchor="middle" font-family="serif" font-size="{size}">{label}</text>'
items=[]
for col,file,title in [(0,'017/equality.json','Equality: same terminal color'),(1,'012/gadget.json','Inequality: distinct terminal colors')]:
    ps=[tuple(F(*c) for c in p) for p in json.loads((root/'rounds'/file).read_text())['centers']]
    assert len(ps)==35
    points=[(float(x)*75+45+col*300,240-float(y)*75) for x,y in ps]
    items.append(text((150+col*300,20),title))
    for i,p in enumerate(ps):
        for j,r in enumerate(ps[:i]):
            if sum((a-b)**2 for a,b in zip(p,r))<=1:items.append(line(points[i],points[j],'#ccc'))
    for i,p in enumerate(points):items.append(circle(p,5 if i>=33 else 3,'white' if i>=33 else '#333'))
    for label,p in zip(['s','t'],points[-2:]):items.append(text((p[0]+12,p[1]+5),label))
svg('primitives.svg',600,305,items)
items=[]
for y,kind in [(65,'Equality unit'),(180,'Inequality unit')]:
    ps=[(0,y),(52,y)]
    ps+=([(102,y),(142,y-30),(192,y-30),(232,y),(282,y)] if y==65 else [(102,y),(153.5,y),(180.5,y),(232,y),(282,y)])
    ps.append((334,y));ps=[(x*1.5+30,yy) for x,yy in ps]
    for i,(a,b) in enumerate(zip(ps,ps[1:])):
        unequal=y==180 and i==3
        items.extend([line(a,b,'#222','5 3' if unequal else ''),text(((a[0]+b[0])/2,(a[1]+b[1])/2-8),'I' if unequal else 'E')])
    items.extend(circle(p,3,'white') for p in ps)
    items.extend([text((100,y+27),kind),text((530,y+27),'334q')])
svg('wires.svg',570,220,items)
p=[(40,35),(200,35),(360,35),(40,105),(200,105),(360,105),(120,175),(280,175),(440,175)]
edges=json.loads((root/'rounds/027/gadgets.json').read_text())['clause_edges'];assert len(edges)==10
items=[line(p[a],p[b],'#333') for a,b in edges]
for i,point in enumerate(p):items.extend([circle(point,10,'white'),text((point[0],point[1]+4),str(i),12)])
for i in range(3):items.append(text((p[i][0],15),'literal '+str(i+1),12))
items.append(text((430,208),'output = True',12));svg('clause.svg',510,220,items)
print('Three exact-data vector figures generated; no plotting dependency required.')
