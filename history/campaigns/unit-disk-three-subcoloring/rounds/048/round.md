# Round 048 — complete rational-detour wire

## Plan

Use a 334q unit: two 52q hub arms plus a 230q interior. Equality interiors
are five length-50q cells in directions horizontal, (4/5,3/5), horizontal,
(4/5,-3/5), horizontal with states 4,5,4,4,5. Inequality interiors are
50q,51.5q,I(27q),51.5q,50q along the line; use the prior connector's color
orientations. Test four directions and all nine endpoint color pairs, with
both one and two grid units (72 motifs). Subsequent units use two 52q cells
around another equality detour. Check complete witnesses and induced copies.
New issue: three-cell paths and interaction across unit boundaries. Reuse
round 047's repaired color states and all prior primitive forcing evidence.
Stop at the first saved counterexample or all 72 passing tests.

## Evidence and diagnosis

All 72 complete segment witnesses pass, with every primitive induced; see
[output.jsonl](output.jsonl). Command: `python3 rounds/048/probe.py` from the
campaign directory. Zero solver queries, repairs or reruns. The rational
kink repairs the length mismatch with seven equality-cell slots per grid
unit; an inequality replaces one slot by I. The projected count is now
137v+238ell-69e, independent of the equality/inequality labels.
Experience extraction: pending composition entry records the rational detour
and its nontrivial internal-color states. Shared writes remain blocked.
Next: test branching junctions and derive a finite-neighborhood proof rather
than assuming straight-wire separation bounds still apply.
