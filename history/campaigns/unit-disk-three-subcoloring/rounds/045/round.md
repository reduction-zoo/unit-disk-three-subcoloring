# Round 045 — restrict buses to incident columns

## Plan

The original crossbar propagates every vertex through every edge column,
including regions beyond all its incidences. Keep a horizontal bus only
between its first and last incident edge columns. When a vertical channel
crosses an absent bus, use a straight equality segment instead of a crossover.
Recover a vertex at its first incident column. Source graphs have no isolated
vertices; check that premise rather than adding an unused fallback.
Test all six prepared source instances with independently solved network
constraints and source predicates, six color permutations per YES case.
Also check integer-grid segment intersection and degree premises, and report
projected geometric sizes under both spacings. A bad intersection or decision
mismatch rejects the compiler. Existing compressed-variable experience and
source/network evidence apply; no new shared finding is assumed.

## Evidence and diagnosis

All six independent network decisions and all 24 YES color-permutation
recoveries pass in [output.jsonl](output.jsonl). All six grid-intersection
checks pass with maximum degree four. Command: `python3 rounds/045/probe.py`
from the campaign directory. Twelve decision queries (six network, six source),
no repairs or reruns. Counts are projected geometry, not emitted targets.
Clipping reduces crossings but does not remove the million-vertex bottleneck.
An additional, unplanned diagnostic computed standard reverse Cuthill--McKee
edge-span totals on the six prepared source graphs: 4→4,47→41,113→84,62→55,
239→164,273→226. This is not a separately claimed research round or proof;
it was executed before a new round declaration and supplies only a layout lead.
Experience extraction: pending geometric-composition update for incident-range
clipping and its checked recovery premise. Shared writes remain outside scope.
Next: audit whether the large source graph is an artifact of unnecessary
routing crossings, before building a large verification implementation.
