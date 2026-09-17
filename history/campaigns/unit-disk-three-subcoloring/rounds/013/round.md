# Round 013 — two-copy geometric chains

## Plan

Hypothesis: copies of the 35-vertex inequality gadget can share terminals while
preserving all proper colorings of the corresponding edge path. Place global
terminals at (0,0),(2,0),(4,0). Independently reverse each edge's gadget endpoints
and reflect its interior across its edge, giving 16 placements. For each, test
terminal patterns (0,1,0) and (0,1,2), both without and with clean global terminals.
Scope: 64 solver queries on 69-vertex graphs plus canonical witness checks.
Validate each embedded copy is an induced copy of the original gadget using
exact rational distances. Shared vertices are only declared terminals; coincident
interior centers stay distinct vertices. No timeout.

Use the pending clean-terminal finding and round 012's concrete gadget. Global
cross edges are allowed in this experiment but must be checked, not ignored.
A successful path would not by itself propagate equality over arbitrary distance.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/013/probe.py`.
[Output](output.jsonl): 64 queries on 16 placements. Actual cross edges are
included and every embedded copy is checked against the original adjacency.
The output records ordinary and clean feasibility separately. Valid canonical
witnesses demonstrate direct extension without a source-solving oracle.
No 3-SAT injection or recovery calls; no repair/rerun; usage unavailable.

Reflection and endpoint orientation affect feasibility. Some placements retain
both path color patterns with clean global terminals; other placements are
infeasible. Thus arbitrary geometric gluing is invalid, while selected placements
can realize a two-edge path. This is not yet equality transmission: both equal
and different outer-terminal colors can occur in the successful path layouts.

Experience extraction: update the pending terminal-composition finding with
actual geometric cross-edge checks. Finite successful placements and failed
placements coexist; do not state that all reflected chains work. No new entry.

## Next action

Build a geometric triangle from three inequality gadgets to obtain three
pairwise-different clean ports. Test only outward-facing interiors, with all
eight choices of endpoint orientation. Use rational triangle coordinates and
verify that slight diagonal compression preserves every local adjacency.
This is the next prerequisite for an equality diamond and a scalable wire.
