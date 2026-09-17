# Round 030 — distinguish crossover witness failure from infeasibility

## Plan

Round 029 only rejected canonical witnesses. Solve both clean signal patterns
for the 16 geometrically distinct state pairs (state IDs 0,2,4,6). Query budget
32, on the same 70-vertex midpoint crossing. Any layout accepting both patterns
would support an extendible crossing candidate; one missing pattern rejects
that layout as a clean crossover. Reuse the local composition diagnosis; no
new shared entry applies. Exact rational adjacency, no timeout.

## Evidence and diagnosis

All 32 clean extension queries are UNSAT. Thus none of these 16 midpoint
geometries supports either pinned clean boundary pattern. This is stronger
than the canonical failure but still only excludes this fixed crossing family.
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/030/probe.py`;
[output.jsonl](output.jsonl) preserves all statuses. No source injections or
recovery calls, no repairs; time/token unavailable.

Experience extraction: extend pending geometric-composition with the precise
16-layout clean-crossing exclusion. No shared write under campaign restriction.
Next use the published planar crossover and attempt a fixed orthogonal layout
with installed Graphviz; check actual intersections rather than trusting layout.
