# Round 047 — rational kink instead of long length adjustment

## Plan

A three-cell equality path with 50q cells directed (4/5,3/5), (1,0), and
(4/5,-3/5) spans 130q. Two straight equality cells of length (103/2)q plus
one 27q inequality cell have the same span. This could replace a nine-cell
length adjustment by three cells. First test the four ordered kink directions
between horizontal and either rational diagonal, with all 16 state pairs
from {0,1,4,5}, using 50q cells: 64 motifs. Record induced-copy preservation
and complete clean witness validity. Failure only excludes the tested
canonical witness states, unless induced-copy geometry itself fails.
Experience: round 042 covers straight chains only; no diagonal composition
is inferred. Completion: 64 exact checks and a decision on this mechanism.

## Evidence and diagnosis

All 64 motifs retain induced copies; 56 clean
canonical witnesses pass. The all-state-4 choice fails at horizontal-to-up
and down-to-horizontal kinks. These failures are witness failures, not a
geometric obstruction: swapping the two nonterminal colors (state 5) repairs
the relevant pair without changing its coordinates. See [output.jsonl](output.jsonl).
Command: `python3 rounds/047/probe.py` from the campaign directory; zero solver
queries, repairs or reruns. Experience extraction: pending composition entry
must distinguish internal-color compatibility from shape compatibility, with
these counterexamples retained as regression motifs. Shared writes blocked.
Next: compose the whole five-cell detour between endpoint hubs; pair checks
alone do not exclude a P3 involving three cells.
