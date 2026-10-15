# Candidate reduction argument

The candidate maps 3-SAT to three-subcoloring of rational unit disk graphs.
Its forward and recovery commands are implemented in [algorithm.py](algorithm.py).
The argument below depends on computational forcing lemmas and an unreviewed
geometric composition argument. Nonempty full-source outputs have not passed
independent target solving. This is not a verified campaign result.

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

The crossbar gives each proper-graph vertex a horizontal bus and each edge a
vertical channel. A nonincident bus/channel crossing receives the fixed
crossover. Equality joins the lower endpoint to the channel; inequality joins
the channel to the upper endpoint. Reading one bus color per source vertex
recovers a proper coloring from every satisfying network coloring. Conversely,
a proper coloring extends through each crossover independently.

The fixed crossover occupies a 40-by-40 integer cell after two short port
extensions. Its interior is noncrossing. North/east boundaries contain portions of the
internal drawing; south/west padding separates neighboring interiors. The
64 ordered adjacent/diagonal cell-type checks in round 040 verify that all
contacts are shared endpoints and every resulting degree is at most four.
Cells outside these relative positions are disjoint. Thus the generated network satisfies the
premises of the geometric lemma for every source, rather than only for the
six instances checked in [round 036](../rounds/036/round.md).

## Geometric map and decision equivalence

The [composition lemma](../rounds/037/composition.md) gives exact coordinates
for any such orthogonal network. It uses equality cells of lengths 52q and
53q, an inequality cell of span 27q, and junction spacing 1535q, where
q=749/10000. Its distance-two bounds reduce every possible cross-copy
monochromatic path to a checked local motif. Reading central junction colors
recovers every network constraint from any valid target coloring.

Combining the source, network and geometric implications proves the proposed
YES/NO equivalence, conditional on the finite forcing lemmas and the composition
argument. In particular, NO instances still receive valid center lists. The
coordinate emitter never receives an assignment, invokes a solver, or chooses
steps using an LLM. [Round 038](../rounds/038/round.md) checks this emitter against
the saved macro and constructs an inconsistent network without a witness.

An empty clause list maps to the empty graph and recovers the all-false sparse
assignment. Malformed source strings map to JSON null, which the target language
rejects. These branches do not establish correctness of nonempty formulas.

## Universal recovery

The forward map emits all junctions in sorted coordinate order before filling
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
ell and h inequality segments, the emitted vertex count is exactly

    137v + 986ell - 69e + 34h.

The hub contribution is 137v. A k-unit segment has 29k-2 free equality cells;
its interiors add 34(29k-2)-1 vertices, plus 34 when it includes I. This counts
shared endpoints once. The formula matches the emitted macro and rectangles.
The resulting source target has fewer than 110,000,000(m+1)^2 vertices.
The large constant is material to verification despite polynomial asymptotics.

Primitive denominators are fixed, and translations use integer grid positions.
Each coordinate therefore needs O(log(m+2)) bits. Total output size is
O((m+1)^2 log(m+2)), bounded by O((L+1)^3). Sorting active labels and using
schoolbook exact arithmetic give a conservative O((L+1)^4) forward time bound.
Recovery reconstructs only the network and reads the target witness. Its
runtime is polynomial in L plus witness length; O((L+|w|+1)^4) is a conservative
bound. Sparse recovery emits at most t variable entries, of total size O(L).

## Outstanding verification

The actual-target CP-SAT tests in [round 039](../rounds/039/round.md) cover a
4,216-vertex YES network and a 4,250-vertex NO network. Full-source subprocess
tests cover empty formulas, compressed declarations and malformed inputs.
They do not cover a nonempty source through independent solving of its complete
geometric output. The smallest prepared nonempty case would emit 19,324,556
vertices. The current dense source harness cannot represent that adjacency
matrix, and the small sparse experiments do not establish that a full solver
encoding fits this 16-GiB machine. No doomed full run or OOM is claimed.

No independent reviewer, advance decision or publication manuscript exists.
The next verification strategy must address these actual output sizes and
preserve independent checking of the emitted target. A complete-source test
cannot be replaced by assuming the reduction's own composition lemma.
