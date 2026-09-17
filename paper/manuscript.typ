#import "report.typ": research-report
#show: research-report.with(
  title: "Three-Subcoloring of Rational Unit Disk Graphs",
  date: "16 September 2026",
  status: "Computer-assisted result — awaiting expert review",
)
#set math.equation(numbering: "(1)")
#let lemma(name, body) = block(breakable: true)[*#name* #body]

#heading(numbering: none)[Abstract]
A subcoloring partitions a graph into color classes, each inducing a disjoint
union of cliques. We give a deterministic polynomial-time reduction from 3-SAT
to three-subcoloring of unit disk graphs supplied by rational centers. The
construction combines two constant geometric gadgets with planar signal routing.
A locality argument extends their finite coloring certificates to arbitrary
formula sizes. Every valid target coloring yields a satisfying assignment in
polynomial time, without assumptions about its internal gadget colors.
The output has quadratic vertex count in the number of clauses and logarithmic
coordinate bit length. The result is computer-assisted: finite forcing claims
are checked by independently encoded solver queries, without formal UNSAT proof
traces. It addresses a question explicitly posed by Marin and Watrigant; priority
remains subject to the literature coverage described below.

= Introduction
Three-subcoloring permits a monochromatic edge but forbids a monochromatic
induced path on three vertices. This relaxation makes ordinary proper-coloring
gadgets unsuitable without additional control over their interfaces. In unit
disk graphs, interfaces must also admit a geometric realization with a common
adjacency threshold.

Marin and Watrigant [1, Section 6] ask for the complexity of three-subcoloring
of unit disk graphs. Their two-color hardness theorem does not settle this
question: a third color may make a previously infeasible instance feasible.
Their results for larger graph classes likewise do not supply the required
unit disk representations. The subsequent work [2] inspected here concerns
two-subcoloring algorithms and lower bounds.

#lemma("Theorem 1 (computer-assisted).", [There are deterministic polynomial-time
maps $f$ and $g$ from 3-SAT to three-subcoloring of rationally represented unit
disk graphs such that
$ phi in "3-SAT" <==> f(phi) in "3-Subcoloring", $
and every valid three-subcoloring $w$ of $f(phi)$ gives a satisfying assignment
$g(phi,w)$. For a formula with $m$ clauses, the output has fewer than
$110\,000\,000(m+1)^2$ vertices, each coordinate uses $O(log(m+2))$ bits, and
the represented target language is NP-complete.])

The new component is the rational unit disk realization of composable equality
and inequality constraints. We reuse the published proper-coloring clause and
crossover constructions of Garey, Johnson and Stockmeyer [3]. The large output
constant limits practical instance sizes; it does not affect the Karp reduction.
The finite lemmas below are computational claims about explicit constant objects.
The proof for arbitrary formulas rests on their composition and geometric locality.

= Languages and fixed geometric gadgets
A target instance is a finite list of centers $p_i in QQ^2$, encoded by signed
binary numerators and positive binary denominators. Distinct indices are adjacent
exactly when $norm(p_i-p_j)^2 <= 1$. Coincident centers are allowed. A valid
witness assigns colors in $\{0,1,2\}$ and contains no monochromatic induced
$P_3$. Equivalently, every monochromatic connected component is a clique.
This witness property is hereditary under induced subgraphs.

A source formula has three literals per clause; repetitions and tautologies
are allowed. Only variables appearing in clauses are used. A sparse assignment
lists their truth values and assigns false to all omitted variables. This
convention matters when the declared number of variables is a large binary
integer.

== Exact coordinates and terminal relations
Both primitives have the same 33 internal centers. In units of one fifth,
these are the pairs $(a,b)$ described by
#table(columns: (1fr, 4fr), inset: 4pt, stroke: .4pt + luma(75%),
  [$a$], [$B_a$],
  [$2$], [$\{4,6,8\}$],
  [$4$], [$\{2,4,6,8,10,12\}$],
  [$6,8$], [$\{0,2,4,6,8,10,12\}$],
  [$10,12$], [$\{2,4,6,8,10\}$],
)
where each pair contributes $(a/5,b/5)$ for all $b in B_a$.
The equality primitive $E$ adds terminals $(12/5,-3/5)$ and $(-1/5,12/5)$.
The inequality primitive $I$ adds $(2/5,-2/5)$ and $(12/5,-2/5)$.
@primitives shows their exact induced graphs.

#figure(image("figures/primitives.svg", width: 100%), caption: [The two
35-vertex primitives at their original coordinates. Every edge is drawn using
exact squared-distance comparison. Hollow vertices are the terminals $s,t$;
filled vertices are internal. Their admissible terminal relations differ even
though their internal center sets coincide.]) <primitives>

#lemma("Lemma 2 (finite forcing).", [Every three-subcoloring of $E$ gives equal
terminal colors, and every three-subcoloring of $I$ gives distinct terminal
colors. Each allowed terminal assignment extends to a coloring in which neither
terminal has a neighbor of its own color.])

*Computational proof.* Introduce one variable $c_v in \{0,1,2\}$ for each
vertex. For each induced path with center $v$ and endpoints $u,z$, impose
$ not (c_u = c_v and c_v = c_z). $
Append the forbidden terminal relation. Independently written Z3 and CP-SAT
encodings return UNSAT. Saved complete colorings satisfy the allowed relation
and the clean-terminal condition; color permutations give every allowed assignment.
The appendix identifies the coordinates, witnesses and independent checker.
These computations trust the solver implementations. Retained constraint kernels
are not independently checked formal UNSAT traces.

To place $E$ along a segment, normalize its terminals to $(0,0),(1,0)$ by a
rational similarity. For terminal displacement $d$ and squared length $D$,
a center $p$ has normalized coordinates
$ x = ((p-s) dot d)/D, quad y = det(d,p-s)/D. $
A reversed copy uses $(1-x,-y)$. Pairwise exact comparisons show that the
induced graph is unchanged when its squared terminal span lies in
$(394/29,394/25]$. Put $q=749/10000$. The squares of the spans $50q$, $(103/2)q$ and $52q$
lie in this interval. The inequality copy at span $27q$ also preserves its
induced graph. All transformations below are rational.

= From formulas to a planar constraint network
Construct a proper-three-coloring graph with a palette triangle labeled True,
False and Base. Each mentioned variable has two adjacent literal vertices,
both adjacent to Base. A proper coloring therefore assigns them opposite
truth-palette colors.

For each clause attach the component in @clause. Its literal ports
are vertices $0,1,2$, its six internal vertices are $3,\ldots,8$, and vertex
8 is joined to False and Base. Its internal edge set is
$ \{03,14,25,34,36,46,67,57,58,78\}. $
The notation $i j$ denotes the unordered edge with endpoints $i,j$.
All eight Boolean boundary assignments have been independently checked: an
extension with output True exists exactly when at least one literal is true.
This is the clause relation of [3, Theorem 2.1]. Identifying repeated literal
ports restricts that relation, so repetitions and tautologies require no new case.

#figure(image("figures/clause.svg", width: 82%), caption: [The published clause
component used before geometric compilation. All ten component edges are shown.
Palette edges from vertex 8 to False and Base are omitted and force its color
to True. The three top ports are identified with the clause's literal vertices.]) <clause>

Assign one horizontal row to each proper-graph vertex and one vertical column
to each edge, in deterministic index order. The horizontal bus spans its first
to last incident column. The edge channel spans its endpoint rows, with an
equality connection at its lower endpoint and an inequality connection at its
upper endpoint. A crossing of a nonincident active bus and channel receives
the fixed planar crossover of [3, Theorem 2.2]. Its opposite terminals agree,
and its two signal colors are independent, including when they coincide.
A crossing with an absent bus is a straight equality connection.

The fixed orthogonal routing certificate replaces vertices of excessive degree
by equality cycles. Its 49 junctions and 64 segments have degree at most four
and no intersections except shared endpoints. All 81 crossover boundary
assignments are checked independently. The drawing fits a constant integer
cell. South and west padding separates interiors of adjacent cells; north and
east outlets meet only the prescribed neighboring ports. The exact ordered
paths are supplied as fixed data with the algorithm.

Finally replace each distinct horizontal coordinate by its sorted rank, and
do the same vertically. These strictly increasing maps preserve every equality
and comparison that defines an axis-aligned segment intersection. The compacted
network therefore has integer coordinates and the same constraints. Each source
vertex is represented by the left port at its first incident column.

#lemma("Lemma 3 (source equivalence).", [A formula is satisfiable exactly when
its planar network admits three colors satisfying each equality and inequality
constraint. Every satisfying network assignment decodes to a source assignment.])

*Proof.* Extend a satisfying assignment to the literal and clause graph, then
through each independent crossover. In the reverse direction, the connected
horizontal buses carry a single color and every original edge channel forces
its endpoint colors to differ. Restrict to the proper graph and compare each
positive literal with True. The clause relation makes every clause satisfied.
The fixed crossover constraints and coordinate ranking preserve both arguments.

= Rational geometric compilation
Place a four-arm junction at each network vertex on a grid with spacing
$S=334q$. Each arm is a reversed equality copy with terminal span $52q$.
All four copies share their central terminal. A junction contributes 137
vertices. Missing network directions retain these short arms and omit their
continuations.

A grid unit along a network segment has two endpoint arms and a five-cell
connector, as shown in @wires. For equality the connector consists of
five length-$50q$ equality cells in directions
$ (1,0), quad (4/5,3/5), quad (1,0), quad (4/5,-3/5), quad (1,0). $
Their displacement is $230q$. For inequality the collinear connector has
successive spans
$ 50q, quad (103/2)q, quad 27q, quad (103/2)q, quad 50q, $
with $I$ in the middle and $E$ elsewhere. Both connectors fit the same grid
unit. Rotate the construction into the segment direction.

#figure(image("figures/wires.svg", width: 100%), caption: [Terminal skeletons
of one equality unit and one inequality unit. A solid segment denotes a copy
of $E$; the dashed segment denotes $I$. Hollow points are shared terminals.
Internal gadget vertices and their edges are omitted. The first and last
segments are junction arms. The detour preserves rational coordinates while
matching the inequality connector's endpoint displacement.]) <wires>

For an integer-length network segment of length $k$, use the indicated first
unit and $k-1$ equality units. At a boundary without a network junction, use
two collinear $52q$ equality cells. The deterministic map emits all junctions
in sorted coordinate order before all wire interiors. It depends only on the
formula and fixed rational data, and invokes no solver.

== Simultaneous coloring and locality
The finite extension certificates give colors for every endpoint relation.
For the equality detour, the five copies use states $4,5,4,4,5$ in the fixed
primitive-state enumeration supplied with the artifact. States 4 and 5 have
identical geometry and exchange the nonterminal colors. The inequality connector
uses its saved clean terminal permutations. These choices agree on all shared
terminals for any satisfying network assignment.

#lemma("Lemma 4 (geometric extension).", [Every satisfying assignment of the
network constraints extends to a three-subcoloring of the complete emitted graph.])

*Proof.* A three-vertex path in a unit disk graph has Euclidean diameter at
most two. The exact support checks place each unit and its endpoint hubs within
distance $90q$ of the supporting grid segment. Nonincident supporting unit
segments have distance at least $334q$, leaving point separation
$ 334q-180q > 2. $
Consequently a path can involve only a single local unit neighborhood,
consecutive units of one wire, or units incident at a common junction.

At a junction, the five-cell interiors of distinct first units are pairwise
farther than two apart. The independent checker verifies all 96 constant
geometric cases: distinct arm directions, either orientation and either relation
type, including connector terminals. Later units are excluded by the support
gap. A path at the junction therefore contains interior vertices from at most
one incident wire. The entire central hub plus that wire occurs in the exact
one- and two-unit endpoint checks, which cover every endpoint color and all
four directions. Other incident arms contribute only hub vertices to this
neighborhood. This covers incoming as well as outgoing wires and all mixtures
of the two relations.

Inside a longer wire, a path away from a unit boundary occurs in a checked
one- or two-unit pattern. At a boundary the same pair of collinear $52q$ state-4
cells is emitted, independent of the boundary index. The five-cell connectors
begin at distance $52q>2$ from that boundary. A path straddling it lies in the
width-four strip centered there; its translated geometry and coloring are
identical to the checked two-unit strip. A diameter-two path cannot meet both
boundary neighborhoods of a middle unit. The first inequality unit's boundary
with the equality suffix is included in the two-unit checks. This establishes
the assertion for arbitrary lengths; additional three- to five-unit checks
are supplementary evidence.

Every possible induced path thus lies in a constant neighborhood where the
stated simultaneous coloring was checked. None is monochromatic, proving the
lemma.

= Decision equivalence and recovery
*Proof of Theorem 1.* A satisfiable formula has a satisfying network assignment
by Lemma 3, and Lemma 4 extends it to the emitted unit disk graph. Conversely,
restrict any valid target coloring to each induced primitive. Lemma 2 forces
the appropriate equality or inequality relation regardless of the primitive's
other colors. Transitivity along each wire yields a satisfying network assignment,
and Lemma 3 recovers a satisfying source assignment. Extra inter-gadget edges
cannot remove an induced path within a primitive. This argument uses no
clean-terminal or canonical-color premise on the supplied witness.

Recovery reconstructs only the network. If a junction has zero-based rank $j$
in sorted coordinate order, its central target vertex has index $137j$: each
previous junction contributes 137 vertices, its center is emitted first, and
distinct hubs share no terminal because grid spacing exceeds twice the arm
length. Read the center colors at the source bus representatives, then compare
each positive literal's color with True. This gives an explicit universal
recovery map, with no source solving step.

An empty formula maps to an empty center list and recovers the empty sparse
assignment. Malformed source encodings map to the rejected target value
`null`. Every well-formed NO formula uses the same geometric construction as
a YES formula. Exact rational comparisons and enumeration of vertex triples
check target witnesses in polynomial time, giving membership in NP.

== Size and time
Let $L$ denote source encoding length, $m$ the clause count and $t$ the number
of mentioned variables. Since $t<=3m$, the proper graph has at most $3+12m$
vertices and $3+21m$ edges. The crossbar has at most $252(m+1)^2$ constant
cells. A cell has at most 51 junction sites and total segment length 414;
coordinate ranking cannot increase lengths.

#block(breakable: false)[
For $v$ network junctions, $e$ segments and total integer segment length $ell$,
the exact emitted vertex count is
$ N = 137v + 238ell - 69e. $
]
A length-$k$ segment has $7k-2$ free primitives, and both primitive types have
35 vertices. Shared terminals leave $34(7k-2)-1$ new vertices beyond the hubs.
Summing proves the count and the numerical bound in Theorem 1.

All primitive denominators are fixed. Integer translations range over a box
of side $O(m+1)$, so each coordinate has $O(log(m+2))$ bits. Total output
encoding size is $O((m+1)^2 log(m+2))$, bounded conservatively by $O((L+1)^3)$.
Sorting active labels and using schoolbook rational arithmetic gives forward
time $O((L+1)^4)$. Recovery takes $O((L+|w|+1)^4)$ time for witness encoding
$w$ and emits at most $t$ entries of total size $O(L)$. These bounds do not
iterate over the magnitude of the declared variable count.

= Scope and limitations
The result supplies a complete geometric reduction and universal witness
recovery. Its proof uses finite solver-checked forcing claims and exact local
geometry. Formal UNSAT traces or human proofs of the finite forcing lemmas
would reduce the trusted computational base. Neither solver agreement nor an
agent review replaces expert scrutiny of the construction and proof.

The literature search on 16 September 2026 covered the explicit open question
in [1], equivalent cluster-partition formulations, [2], the source constructions
in [3], and the accessible abstract of [4]. No settling result was located.
The full theorem content of [4], unindexed work and a complete citation-chain
search remain outside coverage. The application abstract alone does not imply
fixed-three recognition hardness. These limitations qualify priority, rather
than the definitions or the theorem's correctness requirements.

#heading(numbering: none)[References]
[1] Malory Marin and Rémi Watrigant. _Subcoloring of (Unit) Disk Graphs._
MFCS 2025, LIPIcs 345, Article 74.
#link("https://doi.org/10.4230/LIPIcs.MFCS.2025.74")[doi:10.4230/LIPIcs.MFCS.2025.74].
Theorem 7 and Section 6; full version arXiv:2506.19452v1.

[2] Malory Marin and Rémi Watrigant. _Small Independent Sets versus Small
Separator in Geometric Intersection Graphs._ 2026.
#link("https://arxiv.org/abs/2604.26533")[arXiv:2604.26533v1]. Sections 4.1 and 5.2.

[3] Michael R. Garey, David S. Johnson and Larry Stockmeyer.
_Some simplified NP-complete graph problems._ Theoretical Computer Science
1 (1976), 237–267.
#link("https://doi.org/10.1016/0304-3975(76)90059-1")[doi:10.1016/0304-3975(76)90059-1].
Theorems 2.1 and 2.2, pp. 248–250, Figures 1 and 2.

[4] Malory Marin, Joachim Cendrier, Loïc Chassin de Kergommeaux,
Rémi Watrigant, Thomas Begin and Anthony Busson. _Fair radio channel assignment in WLANs via graph subcoloring._
Computer Networks 276 (2026), Article 111990.
#link("https://doi.org/10.1016/j.comnet.2026.111990")[doi:10.1016/j.comnet.2026.111990].
Accessible abstract inspected; full theorem coverage unresolved.

#pagebreak()
#set heading(numbering: "A.1.")
#counter(heading).update(0)
= Verification and reproducibility
All paths in this appendix are relative to
`campaigns/unit-disk-three-subcoloring/` unless stated otherwise.
The computational supplement is part of the argument: preserve the campaign
with its fixed data dependencies when reproducing the result. Python 3 with
Z3, OR-Tools, NumPy and SciPy is required for verification. The two reduction
maps themselves use only the Python standard library. Typst compiles this paper;
`work/figures/draw.py` generates its SVG figures using exact data.

== Fixed data and proof checks
The primitive coordinates are in `rounds/017/equality.json` and
`rounds/012/gadget.json`; allowed clean colorings and state enumeration are
retained in rounds 012, 017 and 018. Clause edge data are in
`rounds/027/gadgets.json`. The fixed orthogonal paths are in
`rounds/032/routing.json`. The current deterministic network and geometry
implementations are `rounds/051/network.py` and `rounds/051/geometry.py`,
called by `work/algorithm.py`.

The finite proof checks include 72 one- and two-unit colorings in round 048,
81 four-arm stars in round 049, 72 support checks in round 050, and 108 longer
wires with 324 boundary-strip comparisons in round 057. The independent review
checker does not import candidate or campaign checker implementations. Its
saved output in `reviews/compact-construction/check.jsonl` covers the two
forcing relations, scaling, 16 mixed-direction stars, 96 arm-separation cases,
eight clause assignments and 81 crossover assignments. Run from the campaign:
```sh
python3 reviews/compact-construction/check.py
```

== Injected source instances and oracle limits
The integrated prepared suite contains four YES and two NO sources and reports
19 fresh-process recovery calls. Its largest actual emitted target has
4,059,987 vertices. The additional suite tests a nonempty YES and NO with
5,001-digit variable labels, an empty instance, six malformed sources and seven
recoveries. Eight further noncanonical target colorings in round 060 recover
valid source assignments. These are finite coverage statements; repeated
recoveries and color permutations are not independent source instances.

The large-target oracle checks an untrusted list of primitive indices against
the actual rational centers. Every induced primitive graph is recomputed.
Contracting its necessary equality relations and imposing its inequalities
can certify NO when the resulting constraint system is UNSAT. A satisfiable
projection is only unknown. YES requires a complete coloring, checked globally
by verifying that each monochromatic component is a clique in the actual graph.
The restricted phase search can miss a witness; failure is unknown, never NO.
The two integrated harnesses share this partial oracle and are not independent
oracle implementations. Their numeric backend has explicit integer bounds;
it is not an arbitrary-rational decision procedure. Finite oracle self-checks
include 516 geometric comparisons and 5,422 graph/color comparisons.

Saved successful integrated logs are `rounds/060/integrated-self-test.json`,
`rounds/060/prepared-suite.jsonl` and
`rounds/060/additional-verification.jsonl`. To reproduce from the campaign,
choose unused evidence directories:
```sh
python3 work/check.py --self-test
python3 work/check.py --candidate work/algorithm.py \
  --evidence work/evidence/reproduction-prepared
python3 work/verify.py --candidate work/algorithm.py \
  --evidence work/evidence/reproduction-additional
```
These commands use finite declared inputs and no wall-clock timeouts. Full
outputs contain millions of vertices and require substantial memory and disk.
The original successful logs are retained; an editorial change to this paper
does not require rerunning these unchanged suites.

== Forward and recovery command contracts
The source is `{"n":1,"clauses":[[1,1,1]]}` for a positive unit clause with
repeated literals. Each target coordinate is a numerator/denominator pair.
The recovery request contains the original source and a complete target color
list under `target_solution`. In separate processes:
```sh
python3 work/algorithm.py < source.json > target.json
python3 work/algorithm.py --extract < recovery-request.json
```
The recovery output is a sparse Boolean map under `assignment`; omitted
variables are false. Its guarantee assumes a valid coloring of this source's
forward output. It does not assume a coloring produced by the supplied oracle.
Compile from the campaign's `work/` directory:
```sh
typst compile manuscript.typ manuscript.pdf
```
