# Round 011 — external clean ports

## Plan

Hypothesis: a new vertex outside the critical host can carry a forced color
without internal neighbors of that color. Base: critical.json minus vertex 3.
Fix the three pairwise-forced-different anchors (original indices 0,4,18) to
colors 0,1,2; color permutation makes this harmless. Test 60 new points
(x/5,-y/5), x=0,...,14 and y=1,...,4. For each, query all three colors. If
exactly one is feasible, add a cleanliness query for the new vertex. Scope:
180 color queries and at most 60 clean queries. Save geometry and witnesses.
No timeout. A clean port would still need a second exposed port and a layout
with no unintended cross edges for a usable wire.

Use round 010's pending composition condition and the local critical-grid
finding. Do not reuse complete-join or false-twin wires excluded earlier.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/011/probe.py`.
[Output](output.jsonl): 180 color queries (118 SAT, 62 UNSAT); 21 positions
have exactly one feasible color. Of their 21 clean queries, nine are SAT and
12 UNSAT. Total 201 queries over 60 placements. Four clean positions have
anchor color 2 on the left; five have anchor color 1 on the right. All returned
witnesses were checked. No source/recovery calls, repair, or rerun; usage unavailable.

New exposed vertices can satisfy the sufficient clean-port condition that
failed on the original pair terminals. These are separate single-port tests:
two ports added simultaneously may introduce extra P3 constraints, so their
joint feasibility must be checked rather than inferred.

Experience extraction: update round 010's pending terminal-composition entry
with this repair: forcing a new exposed vertex can retain a forced color while
removing same-color interior neighbors. Evidence is finite and specific to the
saved host and coordinates; no general availability claim or review.

## Next action

Test all 20 left/right clean-port combinations jointly, then minimize one
successful inequality gadget while preserving both soundness and clean
completeness. Geometry of repeated copies follows immediately afterward.
