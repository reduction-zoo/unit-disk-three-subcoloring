# Round 007 — larger geometric obstruction threshold

## Plan

Hypothesis: the tested grids were too small for incompatible interior cluster
constraints; three selected larger dense grids may yield a geometric NO
baseline. Test (side, spacing) = (7,2/5), (8,1/3), (9,1/2), in that order.
Scope: exactly three graphs, 49--81 vertices, one three-color query each.
Stop on the first UNSAT graph and retain it for vertex-deletion analysis.
No timeout. This expands round 002's search and therefore counts as a new
round, but is the same obstruction-search idea, not an independent route.

Use round 001's hereditary restriction lemma; no applicable additional shared
entry was found in earlier structure searches. A NO instance could supply
critical extension constraints; it would not itself prove NP-hardness.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/007/probe.py`.
The first grid, 7-by-7 with spacing 2/5, is UNSAT for three subcolors.
[Raw output](output.jsonl), [exact centers](obstruction.json). The declared
first-UNSAT stopping condition applied: one of three templates executed, one
solver query, no source or recovery calls. No timeout, repair, or rerun.
Time/token usage unavailable. The other two templates were not tested.

This is a computationally established geometric obstruction from exact rational
adjacency and the previously cross-checked P3 encoding. It is not yet a human
proof or independently reviewed certificate. It refutes a universal three-color
upper bound subject to the solver/encoding correctness; previous smaller-grid
SAT results must not be generalized. A four-color witness is not yet checked.

Experience extraction: pending proposed entry
`research/experience/rational-grid-three-subcoloring-obstruction.md`, with the
49 rational centers and exact command above. Premise: spacing 2/5, side 7,
adjacency distance <= 1. Use as a NO regression and as a source for critical
gadgets. Computational status only, independent encoding check pending. Shared
write destination remains outside the user-supplied campaign scope.

## Next action

Independently re-encode the NO claim with Boolean color indicators, check four
colors, and greedily delete vertices while preserving UNSAT. A vertex-minimal
obstruction could expose a local extension relation for the next construction.
Short-term prospects improve to unknown from low (uncalibrated); no implication
for complete-reduction feasibility follows from one obstruction.
