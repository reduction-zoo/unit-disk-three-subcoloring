# Independent review of the compact construction

**Decision: advance to manuscript preparation and expert review.**

Review date: 2026-09-16. Candidate: `work/algorithm.py`, using
`rounds/051/network.py`, `rounds/051/geometry.py` and their fixed data dependencies.
The candidate was held unchanged. I wrote only in this review directory and
imported no candidate or campaign checking implementation into my checks.
No new reduction mechanism or research round was introduced.

Correctness is supported as a **computer-assisted general reduction proof**,
with the locality elaboration below. Novelty is supported within the stated
primary-literature search coverage. Significance meets the fixed question.
This decision does not establish publication acceptance or replace human
expert assessment. In particular, the finite forcing computations do not have
independently checked formal UNSAT proof traces.

## Independent evidence

Run from the repository root:

```
python3 campaigns/unit-disk-three-subcoloring/reviews/compact-construction/check.py
```

The final complete execution exited successfully; output is `check.jsonl`.
The check reads fixed rational data and saved finite witnesses, implements its
own exact integer-bucket graph construction, and writes its own Z3 constraints.
It does not import candidate implementations or verification helpers.

- Both 35-vertex primitive forbidden terminal relations are UNSAT. Both saved
  allowed witnesses satisfy all induced-P3 constraints and have clean terminals.
- Equality terminal lengths `50q`, `(103/2)q`, and `52q`, and the inequality
  scaling, preserve their complete induced graphs.
- Sixteen one-unit four-arm stars covering every incoming/outgoing combination
  pass exact P3 validation, with outer colors `(0,1,2,0)` and 1,361 vertices each.
  This is deliberately targeted coverage, not all star color assignments.
- A stronger, color-independent geometric check covers all 96 pairs of distinct
  arm interiors: four directions, either orientation, and either equality or
  inequality geometry. Every point of one interior is farther than two from
  every point of the other. Terminals at the ends of the five-cell connector
  are included in these interiors; the four-arm hub is considered separately.
- The routed crossover has 64 axis-aligned segments and 49 junctions, no
  intersections except shared endpoints (including within an individual path),
  and maximum degree four. All 81 boundary color assignments have precisely
  the required opposite-port equality relation.
- All eight Boolean clause boundary assignments have the required relation
  when the distinguished output is fixed to the true color.

These are finite checks of constant objects. The argument for arbitrary
formulas is the composition and locality proof, not the number of passing tests.

## Correctness

### Source compilation and routing

The edges in `rounds/028/source.py` match the palette/literal construction and
six-vertex clause relation. The independently checked clause relation includes
all-false rejection. Identifying repeated literal ports merely restricts that
relation, so repeated literals and tautologies are covered. A proper coloring
forces each literal pair to take opposite truth-palette colors. Comparing each
positive literal with palette vertex zero therefore recovers an assignment
satisfying every clause.

`rounds/051/network.py` makes each original vertex's active horizontal interval
connected and places exactly one inequality on every original edge channel.
The crossover has independent signals, including equal signals. The finite
routing certificate supports its use in the crossbar. Padding on the south
and west separates adjacent cell interiors; north/east outlets meet the next
cell only at the prescribed ports. Removing inactive horizontal buses leaves
vertical channels with no new crossings. Coordinate ranking is strictly
increasing on each axis and hence preserves every segment intersection and
endpoint equality. It also leaves the representative indices unchanged.
Consequently both directions of the proper-coloring/network equivalence hold.

### Primitive soundness and arbitrary-witness recovery

In `work/proof.md:116`, restriction to each induced primitive is the right
soundness argument. Other gadget vertices and extra inter-gadget edges cannot
remove a monochromatic induced P3 within that primitive. The independently
checked E and I relations imply each wire's endpoint relation by transitivity.
No clean-terminal assumption is used in this direction. Thus every target
witness induces a proper source-graph coloring and a satisfying assignment.

`work/algorithm.py:37` reconstructs the network and reads `137 * rank`.
In `rounds/051/geometry.py`, each hub is emitted before any wire. Its first arm
emits its central terminal first. Four arms add a total of one center, four
outer terminals and 132 interiors, namely 137 vertices. Distinct hubs cannot
share these terminals because spacing exceeds twice the arm length. Their
centers are emitted in exactly the coordinate order used by recovery. The
formula therefore holds for every network, not just the tested rectangle.
Recovery does not solve either decision problem or consult a stored coloring.
Its witness premise is precisely a valid coloring of its own forward output.

### Completeness and the locality obligation

`work/proof.md:99` through `114` compresses the main geometric argument. The
round 049 star program only draws wires directed outward from the central hub;
it alone would not justify every incoming junction configuration. This is not
a discovered counterexample: the stronger independent distance check above
closes this concern. The following elaboration should be retained in the paper.

A P3 in a unit disk graph has Euclidean diameter at most two. Divide wires into
334q-long grid units. Distinct nonincident supporting unit segments have distance
at least 334q, and the 90q support envelopes leave a gap greater than two.
Hence a P3 can meet only one local unit neighborhood, consecutive units, or
units sharing a network junction. Hubs obey the same envelope bound. Sorted-rank
compaction preserves the integer-grid separation premise.

At a junction, the five-cell interiors of different incident first units are
pairwise farther than two, for every orientation and relation type, as checked
independently in the 96 constant cases. Portions beyond the first unit are
already excluded by the support gap. Therefore a P3 at that junction contains
interior vertices from at most one incident wire. The entire central hub plus
that wire occurs in the one/two-unit endpoint checks, with all endpoint colors
and all four directions. The other arms add only their already present hub
vertices locally. This establishes the junction claim also for incoming wires,
all mixtures of equality and inequality, and missing arms. Global cyclic color
permutations account for the central color.

For a long wire, neighborhoods away from internal unit boundaries occur in a
one- or two-unit example. A middle unit can have virtual boundaries on both
sides, but a diameter-two P3 cannot meet both boundary neighborhoods. At an
internal boundary the emitter always uses the same two collinear length-52q
state-4 cells. Their geometry and coloring, translated to that boundary and
normalized by the common terminal color, do not depend on the unit index.
The five-cell connectors begin 52q > 2 from the boundary. Every P3 straddling it
lies in the width-four strip and thus has exactly the checked two-unit local
pattern. This gives the all-length inference; the three-to-five-unit strip
comparisons in round 057 are supplementary finite evidence, not induction by
sample size. The sole inequality unit is first, and the existing two-unit
checks include its boundary with the equality suffix.

Each primitive's geometry is independent of the color permutation. The saved
clean colorings and stated phase choices provide one simultaneous extension of
any satisfying network coloring. The local cases above exclude every possible
monochromatic induced P3 in that extension. This proves completeness for all
network sizes. No solver or random choice appears in the forward map.

### Runtime, encoding, and special cases

The `137v + 238ell - 69e` count follows directly from terminal sharing and
`7k-2` free primitive cells on a length-k segment. The fixed cell has bounded
size and length; the crossbar has O(m²) cells. Ranking cannot increase segment
length. Thus the stated quadratic vertex bound, including the loose numerical
constant, is valid. Coordinates have fixed denominators and O(log(m+2)) bits.
The stated O((L+1)^4) forward and O((L+|w|+1)^4) recovery bounds are conservative
polynomial bounds. Sparse labels avoid work proportional to a binary-encoded
variable declaration. Recovery output has size O(L).

Empty formulas map to the empty graph and the empty sparse assignment. The
JSON-value source validation and rejected-null malformed-input convention agree
with the executable contract. Well-formed NO sources take the same deterministic
geometric construction path as YES sources. The target witness relation is
polynomial-time decidable by exact rational comparisons and triples, so the
hardness statement also yields NP-completeness for the represented language.

## Audit of the injected-instance evidence

I inspected `work/check.py`, `rounds/052/project.py`, `rounds/053/search.py`, the
reports, and the round 060 raw logs rather than rerunning the full suites.
The prepared suite reports four YES and two NO cases and 19 fresh recoveries;
the additional suite reports one nonempty YES, one NO, an empty case, seven
recoveries and six malformed sources. Earlier rounds retain larger finite
coverage and explicit oracle self-checks.

The certificate producer is correctly treated as untrusted. Every used induced
copy is recomputed from the actual emitted coordinates. Equality contraction
and inequality constraints provide necessary target constraints. Their UNSAT
therefore proves NO even if the manifest omits other constraints. A satisfiable
projection supplies no YES conclusion. YES requires a complete coloring whose
monochromatic components are cliques in the actual full graph. Restricted
phase-search failure is unknown, never NO. Thus sharing a certificate producer
or local witness templates with the research process does not invalidate this
logic. It does limit search completeness and diversity, as the reports state.

The integer-coordinate guards make the Chebyshev neighbor query operate on
exactly representable values, followed by exact integer squared distances
within the checked int64 range. This is a bounded numeric verifier for the
actual evidence, not a general arbitrary-rational decision oracle. Both harnesses
share it; their passes are not two independent oracle implementations. My
constant-object graph checker uses Python integers instead. The finite forcing
UNSAT claims still trust mature solver implementations; round 059 cores are
constraint kernels, not formal proof traces. Expert-facing writing must keep
that distinction explicit.

## Novelty and primary literature

Search date: 2026-09-16. Independent queries included `"unit disk"
"3-subcoloring"`, `"unit disk" "subchromatic" three`, `"unit disk graphs"
"partition" "three" "cluster graphs"`, `"unit disk" "3-subcolouring"`, and
`"unit disk" "subchromatic number" "NP" 2026`.

1. [Marin and Watrigant, MFCS 2025](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.74/LIPIcs.MFCS.2025.74.html),
   Section 6, explicitly lists the fixed three-color unit-disk question.
   Theorem 7 is two-color hardness. The co-comparability hardness is on a larger
   class and does not supply unit-disk representations. Neither implies the
   current result. The seven-color upper bound and approximation result also
   leave this exact decision question open.
2. [Marin and Watrigant, arXiv:2604.26533v1](https://arxiv.org/html/2604.26533v1),
   Sections 4.1 and 5.2, concerns two-subcoloring algorithms and lower bounds;
   the inspected scope does not resolve the three-color represented target.
3. [Garey, Johnson and Stockmeyer (1976)](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/JohnsonDavid2.pdf),
   Theorems 2.1 and 2.2, printed pages 248–250, Figures 1 and 2: I inspected the
   archived page images and confirmed the clause/crossover provenance and
   boundary properties. These parts are known; their reuse is not the claimed
   contribution.
4. [Fair radio channel assignment in WLANs via graph subcoloring](https://www.sciencedirect.com/science/article/pii/S1389128626000022?dgcid=rss_sd_all),
   Computer Networks 276 (2026), abstract: the described channel-assignment
   algorithm and upper bounds do not themselves imply exact fixed-three
   hardness. Full theorem coverage of this article remains unresolved.
   [Marin's publication list](https://perso.ens-lyon.fr/malory.marin/publications.html)
   confirms the related publication context, not absence of other results.

No settling result was located within this search. The full WLAN paper,
unindexed work, and complete citation-chain coverage remain limitations, not
positive evidence of novelty. The supported novel component is the rational
unit-disk realization and composable three-subcoloring constraints. The claim
should be stated relative to this search coverage, not as exhaustive priority
certification. I found no theorem implication that makes this merely an
implementation of a known reduction.

## Significance and writing obligations

A complete Karp reduction with universal polynomial witness recovery answers
the exact fixed question. It is a meaningful moderate contribution to geometric
graph complexity even with a large construction constant. Small gadgets alone
would not meet the acceptance criteria; the deterministic routing, locality
argument and bit bounds are essential parts of this result.

No blocking correctness defect was found. The manuscript should expose the
junction and internal-boundary locality reasoning above, identify the finite
lemmas as computer-assisted, preserve the literature limitations, and avoid
calling the solver kernels formal UNSAT certificates. `work/contract.md` still
says nonempty full-source verification is incomplete; that sentence is stale
relative to the inspected round 060 evidence and should be updated in writing.
These are exposition and evidence-status obligations, not requests for a new
mathematical strategy or an additional campaign round.
