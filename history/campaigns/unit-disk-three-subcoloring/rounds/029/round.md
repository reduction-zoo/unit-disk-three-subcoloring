# Round 029 — direct crossing of two equality cells

## Plan

A direct geometric crossover would avoid embedding the published 13-vertex
proper-color crossover. Test 64 ordered state pairs of perpendicular equality
cells at their midpoints, with both equal and different signal colors.
Use length 53q. Check each local induced adjacency and the canonical witnesses.
If any geometry supports both signal relations, save it; otherwise exclude
only these 64 canonical compositions, not all crossover gadgets. The clean
composition experience in rounds 018--025 motivates checking actual cross-edges.
No solver query: this is a witness-family test.

## Evidence and diagnosis

All 64 layouts reject both canonical signal patterns. Raw results in
[output.jsonl](output.jsonl), command `python3 campaigns/unit-disk-three-subcoloring/rounds/029/probe.py`.
This excludes the proposed canonical witness family, not geometric feasibility.
Counts: 128 witness checks, zero solver queries, no repairs or source injections.
Time/token unavailable. Experience extraction: append this bounded failure to
the pending geometric-composition entry; shared destination remains restricted.
Next discriminate witness incompatibility from actual infeasibility using a
solver on the 16 geometrically distinct layouts.
