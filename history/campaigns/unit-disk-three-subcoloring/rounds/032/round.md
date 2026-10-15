# Round 032 — compressed planar crossover certificate

## Plan

Compress distinct x and y coordinates of the checked round 031 drawing to
integer ranks. Strictly increasing coordinate maps preserve all axis-aligned
intersections. Remove redundant collinear path points. Check the graph's
opposite-equality relation for all 81 boundary assignments, including equality
cycle edges, and check every pair of resulting segments exactly. Record its
port locations and path length to expose geometric output size before expansion.
Reuse the verified GJS gadget and fixed drawing, not a general layout heuristic.
The pending composition experience applies; no new shared lemma is assumed.

## Evidence and diagnosis

All 81 mixed-network queries match the crossover relation; nine are SAT.
The compressed certificate has 29 vertices, 44 paths, 64 straight segments,
and total grid length 412 inside a 39-by-39 box. Its port coordinates are
(19,39), (39,19), (19,0), (0,19). Exact segment intersections remain legal.
Raw evidence: [output.jsonl](output.jsonl); certificate: [routing.json](routing.json).
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/032/probe.py`.
No source or full geometric injections, no repairs; time/token unavailable.

Experience extraction: extend pending fixed-template geometric composition
with monotone rank compression; its premise is an already checked orthogonal
drawing. This preserves topology, not distances before geometric expansion.
Next expand straight routes and junction endpoints at a common spacing.
