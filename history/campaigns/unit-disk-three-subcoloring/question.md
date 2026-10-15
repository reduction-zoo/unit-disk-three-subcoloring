---
status: proof-route-hold
openness: supported-within-search-coverage
difficulty: uncertain
importance: moderate
tags: [subcoloring, unit-disk-graphs, geometric-graphs, NP-hardness]
last-literature-check: 2026-09-16
---

# 3-SAT to three-subcoloring of unit disk graphs

## Exact question

Construct a deterministic polynomial-time Karp reduction from 3-SAT to
three-subcoloring of rationally represented unit disk graphs. Input centers
are binary rational pairs; adjacency means squared distance at most one.
A witness assigns one of three colors to each vertex with no monochromatic
induced three-vertex path. Equivalently, each color induces disjoint cliques.
The empty graph is a YES instance; malformed target encodings are rejected.

All well-formed formulas, including NO instances, must map to valid center
lists. Malformed source strings map to a designated malformed target string.
Prove YES/NO equivalence and recover a satisfying assignment from every valid
target coloring in deterministic polynomial time. The completed rule must state
explicit polynomial bounds for runtime, vertex count, coordinate bit length,
and recovery runtime. No construction or exponent is established at screening.
Exact rational distance comparisons and enumeration of vertex triples give a
polynomial target witness checker. A complete rule with general proof and
independent verification qualifies; finite gadgets and failed routes do not.
A polynomial-time target algorithm would not fulfill this positive target.

## Known results and openness evidence

[Marin and Watrigant, MFCS 2025](https://doi.org/10.4230/LIPIcs.MFCS.2025.74),
Section 6, explicitly asks for the complexity of three-subcoloring of unit disk
graphs. Theorem 7 proves two-subcoloring hardness on triangle-free unit disk
graphs and on unit disk graphs of bounded height. Neither implies hardness
with three colors. The co-comparability three-color theorem does not establish
unit-disk representations. Observation 4 gives a seven-color upper bound.

The [full version, arXiv:2506.19452v1](https://arxiv.org/html/2506.19452v1),
Section 4, lifts hardness for arbitrary-radius disks with two copies and a disk
meeting both. Equal radii prevent automatic transfer. Section 4.1 notes that
triangle-free disk graphs have proper three-colorings, so the triangle-free
construction cannot simply be reused unchanged for this target.

The identified [2026 follow-up](https://arxiv.org/html/2604.26533v1), Sections
4.1 and 5.2, studies two-subcoloring algorithms and lower bounds. Its inspected
statements do not settle three colors. The author's
[publication list](https://perso.ens-lyon.fr/malory.marin/publications.html)
was also checked. No resolution was located within this coverage.

Actual queries on 2026-09-16:

- `"3-subcoloring" "unit disk" complexity 2026`
- `"Subcoloring of (Unit) Disk Graphs" "open"`
- `"unit disk" "3-subcolouring"`
- `"unit disk" "subcoloring" "2026"`
- `"unit disk graphs" "subchromatic" "three"`

The original paper, full version, and identified follow-up were inspected.
Cluster-graph partitions and monochromatic induced-P3 avoidance were checked
as equivalent definitions in these sources. Dedicated searches under every
cluster-partition alias and unpublished work remain outside coverage. This
supports openness; it does not guarantee that no solution was overlooked.

## Route and investigation

The provisional route is to force a third color outside Boolean signal
vertices using a local geometric palette gadget, then propagate the two
remaining colors. Palette forcing, propagation, and geometric composition
are not established. Universal recovery would decode signal vertices relative
to the palette, independently of the names assigned to the colors.

A short obstruction excludes unrestricted universal-vertex lifting: three
isolated vertices form a unit disk graph, but two copies plus a universal
vertex form K1,6, which is not a unit disk graph. Among six independent centers
within distance one of a center, two consecutive polar angles differ by at
most 60 degrees. Their radii are at most one, so their squared distance is at
most one, contradicting independence. A coincident center also contradicts
independence. This main-agent proof has not received independent review and
does not exclude local palette constructions.

Shared experience was searched with `subcolor|palette|unit.disk|geometry`.
No applicable established palette construction was found. Scheduling
saturation has different premises and is not used to justify feasibility.
No synthesis experiment or campaign round was run during this selection.

Next bounded task: enumerate point subsets of size at most ten in the 4-by-4
half-integer grid. Check three-subcolorings and terminal pairs for forced
equality or inequality, using exact distance arithmetic and an installed SAT
solver or exhaustive enumeration. Record every feasible terminal assignment.
No timeout is needed for this finite scope. Success would still require
extension and composition proofs; failure excludes only this point family.
This proposed task has not been executed.

## Assessment and screening

Importance is **moderate**: resolve a published complexity case for a standard
geometric graph class. No stronger approximation consequence is claimed.
Difficulty is **uncertain**: the direct color lift fails geometrically and the
remaining mechanism has not been validated.

| Gate | Result | Evidence |
|---|---|---|
| 1. Precise target | pass | Fixed languages, universal recovery, polynomial bound obligations |
| 2. Known implications | pass | Two-color, arbitrary-radius, and co-comparability results differ |
| 3. Openness | pass | Explicit 2025 question; full version and 2026 follow-up checked |
| 4. Significance | pass | Resolve the three-color unit-disk case |
| 5. Proof route | hold | Local palette and propagation unsupported |
| 6. Initial investigation | not assessed | Remaining mechanism not yet validated |

## Research history and campaign handoff

2026-09-16: retained as next screening candidate, distinct from previous cut,
matching, matrix, and scheduling campaigns. Zero candidates admitted in this
selection; one new hold retained. No round allocation is inherited from the
completed scheduling campaign. Begin a campaign after the remaining gates
pass, or explicit user direction to explore the hold. Keep the fixed target,
use exact checks, and distinguish finite evidence from general proofs.
