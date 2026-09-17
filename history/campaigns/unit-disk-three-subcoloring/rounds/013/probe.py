import itertools
import json
import geometry
for reverse in itertools.product((False,True),repeat=2):
    for flips in itertools.product((-1,1),repeat=2):
        t,adj,copies=geometry.compose([(0,0),(2,0),(4,0)],[(0,1),(1,2)],reverse,flips)
        for colors in ((0,1,0),(0,1,2)):
            canonical=geometry.lift(adj,copies,colors)
            for clean in (False,True):
                w=geometry.solve(adj,colors,clean)
                print(json.dumps({'reverse':reverse,'flips':flips,'colors':colors,'clean':clean,
                                  'status':'unsat' if w is None else 'sat','witness':w,
                                  'canonical_valid':canonical is not None}),flush=True)
