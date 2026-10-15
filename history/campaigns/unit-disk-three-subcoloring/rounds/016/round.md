# Round 016 — distinguish auxiliary cleanliness from geometric infeasibility

## Plan

Hypothesis: round 015 failed because auxiliary vertices were unnecessarily
required to be clean. Recheck its exact 64 placements with terminal colors
(0,1,2,2), first unrestricted. For SAT cases, ask only that external ports c,d
have no same-colored neighbors. Stop on the first clean external witness;
otherwise finish the family. At most 128 solver queries, no timeout. Save any
successful graph and witness. The general source target and local inequality
semantics are unchanged. This diagnosis is justified by the previous failure
and avoids enlarging the geometric family before checking its cause.

Use the pending composition finding; no new applicable shared entry.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/016/probe.py`.
[Output](output.jsonl): all 64 placements are UNSAT even without any cleanliness
constraints. Exactly 64 queries; none reaches the conditional clean query.
Given their induced inequality copies, any valid coloring would have skeleton
pattern (0,1,2,2) up to permutation, so pinning that pattern loses no coloring.
The failed diamond layouts themselves are therefore computationally excluded.
No rerun, source/recovery calls, or measured usage.

This rules out the suspected overstrong-auxiliary-cleanliness cause. It supports
actual geometric incompatibility for these 64 placements, not for all equality
diamonds or all wire mechanisms. The passing triangle is retained unchanged.

Experience extraction: update round 010's pending composition finding with the
discriminating check: actual UNSAT persists after removing cleanliness. Do not
claim a new universal obstruction. No new distinct pending entry.

## Next action

Reconsider the need to build equality from a diamond. Search the remaining
perimeter of the original critical host for two widely separated exposed ports
forced to the same palette color, then test joint clean feasibility. Round 011
found such ports only on one boundary; the other boundaries are untested.
