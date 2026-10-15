# Round 014 — geometric three-color triangle

## Plan

Hypothesis: three outward-facing inequality gadgets realize a triangle with
three clean terminals. Coordinates: (0,0),(2,0),(1,433/250), with cyclic edges.
The diagonal lengths are slightly below two. The affine complex-coordinate
map scales/rotates each gadget using rational coefficients; check all internal
adjacencies rather than assuming perturbation is harmless. Test eight endpoint
orientation choices, each keeping interiors outside the triangle. Check the
canonical lifted witness first; if invalid or unclean, ask Z3 for a clean
extension of terminal colors (0,1,2). At most eight queries on 102 vertices.
Soundness follows by restriction to the three induced inequality copies, subject
to the finite gadget lemma. No timeout. Save any valid full geometric gadget.

Use round 013's actual-geometry composition checks and round 012's clean
inequality primitive. A triangle would enable a subsequent equality-diamond
attempt, not complete a 3-SAT reduction by itself.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/014/probe.py`.
The first placement succeeds with the canonical lifted witness; the declared
search stopped at first success. One of eight templates executed, zero solver
queries, one exact full-graph witness check. The [102-vertex triangle](triangle.json)
and [witness](witness.json) have three clean global terminals. All three local
copies retain their original induced adjacency under rational transformations.
The [output](output.jsonl) records the successful orientation. No rerun; usage
unavailable. No source or recovery calls.

Because each edge is an induced inequality gadget, every valid target coloring
assigns three distinct colors to the terminals. The stored clean witness and
color permutation provide completeness for all six distinct-color patterns.
This finite composition claim still inherits the solver-supported base gadget
lemma; it is not independently reviewed and is not a full Karp reduction.

Experience extraction: update the pending terminal-composition finding with
this successful rational geometric triangle and exact canonical extension.
No additional distinct finding file. Earlier infeasible chain placements remain
counterexamples to unrestricted gluing.

## Next action

Construct an equality diamond (K4 minus the edge between the two outer ports)
using five inequality gadgets. If geometrically realizable with clean outer
ports, its two triangles force equal colors at those ports. This supplies a
specific path from inequality to signal transmission.
