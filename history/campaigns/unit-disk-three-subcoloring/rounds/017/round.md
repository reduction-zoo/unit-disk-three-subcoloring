# Round 017 — direct equality ports around the critical host

## Plan

Hypothesis: the same critical host supports two separated clean external ports
with the same forced color, bypassing the failed diamond. Base: critical.json
minus vertex 3, anchors 0,4,18 fixed to 0,1,2. Enumerate the remaining perimeter:
top (x/5,(12+k)/5), left ((2-k)/5,(y-1)/5), right ((12+k)/5,(y-1)/5),
x,y=0,...,14 and k=1,...,4. Deduplicate positions and exclude round 011's tested
bottom positions. At most 180 new positions, three color queries each, and a
clean query only at uniquely forced positions. Reuse all earlier bottom results.

Combine the clean positions by equal forced color, retaining pairs at squared
distance >1. Test the first 12 pairs in decreasing squared-distance order
(lexicographic tie-break), stopping on first joint clean SAT result. At most
732 new queries. Preserve points and witnesses; no timeout. If successful,
verify equality and test serial geometry next. A direct equal-color port pair
is a changed mechanism, not another diamond orientation.

Use the local critical-grid and clean-port findings; no additional shared match.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/017/probe.py`.
[Output](output.jsonl): 172 new perimeter positions; 596 total queries including
the first joint pair. The pair (12/5,-3/5),(-1/5,12/5), both forced to anchor
color 1, has a clean joint witness. Its squared separation is 394/25 > 1.
The [35-vertex equality gadget](equality.json) and [witness](witness.json) retain
the original host and both external ports. The first joint test succeeded;
remaining proposed pairs were not queried. No rerun, source/recovery calls,
or measured usage.

Soundness follows by restriction: each one-port subgraph forces the port's
color relative to anchors 0,4,18, which are pairwise different in every host
coloring by round 009. Thus any joint coloring has equal port colors. The stored
clean witness and color permutation supply all three equal-color assignments.
This inherits finite UNSAT evidence; an unpinned converse check is next.

Experience extraction: update the pending terminal-composition finding with the
direct equality repair, its exact coordinates, and joint witness. This changes
the construction mechanism and avoids the excluded diamond layouts. No new
separate entry or independent review.

## Next action

Check the unpinned equality converse and search period-one/two chains of this
gadget under endpoint reversal, reflection, and the two internal color swaps.
Verify actual two- and three-copy geometry. A projection bound can turn a finite
periodic witness check into an all-length straight-wire lemma.
