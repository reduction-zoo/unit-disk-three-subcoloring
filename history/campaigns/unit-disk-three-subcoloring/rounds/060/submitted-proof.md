# Candidate reduction argument

The candidate maps 3-SAT to three-subcoloring of rational unit disk graphs.
Its forward and recovery commands are implemented in [algorithm.py](algorithm.py).
The argument below depends on computational forcing lemmas and an unreviewed
geometric composition argument. Complete YES and NO source outputs now have certificate-assisted decision
evidence. The general proof and its finite certificates have not received
independent author review. This is a candidate theorem, not a completed campaign.

## Languages and witnesses

The source and target decision languages remain those in [question.md](../question.md).
Their executable encodings are in [contract.md](contract.md). A source witness
is a sparse assignment with omitted variables false. For a binary declaration
n, this avoids requiring an output of length n for a formula of length O(log n).
Only variables mentioned in clauses enter the construction.

A target is a list of rational centers. Two distinct vertices are adjacent
when their squared distance is at most one. A target witness assigns colors
0, 1, 2 and has no monochromatic induced three-vertex path. This property is
hereditary under induced subgraphs, which permits restriction to each gadget.

## Computational forcing lemmas

The 35-vertex [inequality gadget](../rounds/012/gadget.json) forces its two
terminals to differ. The 35-vertex [equality gadget](../rounds/017/equality.json)
forces its terminals to agree. Each allowed relation has a witness in which
neither terminal has a neighbor of its own color. Permuting colors supplies
all allowed terminal assignments.

Z3 and a separately implemented CP-SAT encoding reject the forbidden patterns
and accept the allowed clean patterns. See [round 035](../rounds/035/round.md).
These are exact finite computational claims, with executable reproducers and
coordinates. No independently reviewed proof certificate or human case proof
has been produced. Solver agreement does not establish novelty or significance.

## Source compilation and planar routing

The source graph follows Garey, Johnson and Stockmeyer, Theorem 2.1, with a
palette triangle, opposite literal vertices and a six-vertex clause component.
Its distinguished clause output receives the true palette color. Every proper
three-coloring then decodes a satisfying assignment by comparing positive
literal colors with that palette vertex. Every satisfying assignment extends
to a proper coloring. The executable edge lists and complete clause boundary
checks appear in [rounds 027](../rounds/027/round.md) and [028](../rounds/028/round.md).

The same paper's Theorem 2.2 supplies a planar crossover whose opposite ports
agree and whose two signal colors are independent. We replace high-degree
vertices by equality cycles and use a fixed checked orthogonal drawing.
[Round 032](../rounds/032/round.md) records its exact routing certificate and
all 81 boundary checks. The primary source and theorem locations are recorded
in [round 026](../rounds/026/round.md); these source gadgets are published work.

The crossbar assigns each proper-graph vertex a horizontal bus and each edge
a vertical channel. A bus extends only from its first to its last incident
edge column. Every source-graph vertex has an incident edge. A channel runs
between its two endpoint rows. A nonincident active bus/channel crossing
receives the fixed crossover; a channel crossing an absent bus stays straight.
Equality joins the lower endpoint to the channel, and inequality joins the
upper endpoint. Reading the left port at each bus's first incident column
recovers a proper source coloring from every satisfying network assignment.
Conversely, a proper coloring extends through the crossings independently.

The fixed crossover occupies a 40-by-40 integer cell. Its south/west padding
separates neighboring interiors, including portions on north/east boundaries.
The saved cell-gluing checks certify that intersections are shared endpoints
and degrees are at most four. Removing an inactive bus and replacing its
crossing by a vertical segment introduces no intersection. Replace each
distinct x and y coordinate by its sorted rank. Strictly increasing coordinate
maps preserve every comparison and equality defining an axis-aligned segment
intersection, so the resulting network retains these premises. The compaction
changes neither its constraints nor its representative vertex IDs.

## Geometric map and decision equivalence

Let q=749/10000. The current compiler uses junction spacing S=334q. At each
network vertex it places four equality arms of length 52q. All coordinates
are exact rationals, and every equality copy is a scaled rational rotation
of the fixed E primitive. Its graph is unchanged for squared terminal span
in (394/29,394/25], as checked from every pair of its fixed centers. The
inequality primitive has span 27q and preserves its fixed induced graph.

An equality unit has two 52q endpoint arms and five length-50q cells with
successive directions (1,0), (4/5,3/5), (1,0), (4/5,-3/5), (1,0), rotated
into the network segment's direction. Its interior displacement is 230q.
An inequality unit replaces that interior by collinear cells of lengths
50q, (103/2)q, 27q, (103/2)q, 50q; the middle cell is I and the rest are E.
Its displacement is also 230q. A k-unit segment uses the appropriate first
unit and k-1 equality units. At a junction-free unit boundary, its two
52q arms are collinear equality cells sharing their terminal.

The explicit extension uses the saved clean primitive colorings. The five
cells of a detour have state indices 4,5,4,4,5 in the fixed enumeration from
round 018. States 4 and 5 have the same geometry but interchange nonterminal
colors. The inequality connector uses the fixed endpoint-color permutation
and the color states in round 048. Thus the geometric map depends only on
the network, while the completeness witness depends on its coloring.

Finite exact checks cover all endpoint colors and orientations for one and
two units (round 048) and every four-arm star color pattern up to a global
cyclic color permutation (round 049). The support certificate in round 050
places each unit and endpoint hub within distance 90q of its supporting
segment. Features separated by an integer-grid unit therefore have point
separation at least 334q-180q>2. Such features cannot share a three-vertex
path. Along an edge, only consecutive units can interact; their patterns
occur in the one/two-unit checks. At an incident junction, only its initial
unit neighborhoods can interact across arms; the full-star checks include
these neighborhoods. Missing arms delete downstream vertices. Round 057 also compares every internal boundary strip of three- through
five-unit wires with the two-unit template. The emitter always joins two
collinear 52q state-4 cells at that boundary, so the identity holds for any
number of units. A P3 crossing the boundary lies in its width-four strip;
one meeting nonconsecutive units contradicts the support gap. These facts
give the proposed all-length finite-neighborhood completeness argument,
which remains an explicit independent-review obligation.

For soundness, restrict any valid target coloring to each induced E or I
copy. Their forced relations imply all network constraints by transitivity
along the wires. This uses no cleanliness or canonical-color assumption on
the supplied witness. Composition with the source graph recovers a satisfying
3-SAT assignment. Conversely, the source coloring and the finite-neighborhood
extension give a proposed valid target coloring for every satisfiable source.
The emitter receives no assignment and calls no solver.

Empty formulas map to the empty graph with the all-false sparse assignment.
Malformed source strings map to JSON null, which the target language rejects.

## Universal recovery

The [current forward map](../rounds/051/geometry.py) emits all junctions in sorted coordinate order before filling
segments. Each junction contributes 137 distinct vertices, and its central
vertex is first. Grid spacing exceeds twice the arm length, so different
junctions share no emitted vertex at this stage. The central vertex of the
junction with zero-based rank j therefore has index 137j.

Recovery reconstructs the source network, reads those indices at the original
bus representatives, and applies the source graph decoder. The restriction
arguments apply to every valid target coloring. Recovery assumes neither a
canonical coloring nor a particular solver's output, and it never solves the
source. The rank formula is checked against actual emitted rectangle indices
in [round 040](../rounds/040/round.md).

## Worst-case bit bounds

Let L be the encoded source length, m its clause count, and t the number of
mentioned variables. Then t is at most 3m. The proper graph has at most
3+12m vertices and 3+21m edges, so the crossbar has at most 252(m+1)^2 cells.
Each cell has at most 51 junction sites, total grid-segment length 414, and
24 inequality segments. Coordinates lie in a box of side O(m+1).

For a network with v junctions, e straight segments, total integer-grid length
ell, the emitted vertex count is exactly

    137v + 238ell - 69e.

The hub contribution is 137v. A k-unit segment has 7k-2 free primitive cells;
an inequality segment replaces one E by I, both with 35 vertices. Its interiors
add 34(7k-2)-1 vertices. Shared terminals are counted once. The count matches
the actual full-source outputs in rounds 051 and 054.
The resulting source target has fewer than 110,000,000(m+1)^2 vertices.
The large constant is material to verification despite polynomial asymptotics.

Primitive denominators are fixed, and translations use integer grid positions.
Each coordinate therefore needs O(log(m+2)) bits. Total output size is
O((m+1)^2 log(m+2)), bounded by O((L+1)^3). Sorting active labels and using
schoolbook exact arithmetic give a conservative O((L+1)^4) forward time bound.
Recovery reconstructs only the network and reads the target witness. Its
runtime is polynomial in L plus witness length; O((L+|w|+1)^4) is a conservative
bound. Sparse recovery emits at most t variable entries, of total size O(L).

## Verification scope

[Round 053](../rounds/053/round.md) independently finds and globally checks a
coloring of the actual positive-unit target, then exercises fresh-process
recovery. [Round 054](../rounds/054/round.md) certifies the actual opposite-unit
target NO through checked induced-primitive constraints. The latter inference
needs only necessary local relations, not the completeness argument. The
oracle's finite numeric and logical self-checks are in round 055. Broader
source coverage is recorded in round 056.

The target oracle is certificate-assisted and partial. A checked necessary
projection can prove NO; a complete globally checked coloring can prove YES.
Failure of the restricted internal-color search means unknown. The verifier
does not import candidate code; an untrusted certificate producer supplies
indices that are checked against the actual emitted coordinates. Source
witnesses are validated against the original clauses in separate processes.

General correctness, novelty and significance remain separate review questions.
No independent advance review or publication claim is made here.
