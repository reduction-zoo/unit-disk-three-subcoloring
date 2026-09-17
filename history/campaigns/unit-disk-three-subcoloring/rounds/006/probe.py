import itertools
import json
# The wire has nonadjacent twins within each L bag, complete joins between
# different L bags, and c_i adjacent exactly to its own L bag in this induced set.
vertices=['li','li_prime','lj','lj_prime','ci']
edges={(a,b) for a,b in itertools.combinations(range(5),2)
       if (a in (0,1) and b in (2,3,4))}
assert len(edges)==6
assert sorted(sum(i in edge for edge in edges) for i in range(5))==[2,2,2,3,3]
print(json.dumps({'vertices':vertices,'edges':sorted(edges),'induced_graph':'K2,3',
                  'palette_vertices_used':0,'wire_bags_used':2}))
