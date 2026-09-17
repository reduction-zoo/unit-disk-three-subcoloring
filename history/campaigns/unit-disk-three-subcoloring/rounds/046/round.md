# Round 046 — monotone coordinate compaction

## Plan

Replace each distinct x and y coordinate of the clipped orthogonal network
by its zero-based sorted rank. Strictly increasing coordinate maps preserve
horizontal/vertical segments, all order comparisons, intersections and shared
endpoints. This is a polynomial construction, not an embedding search.
Check all six saved networks, exact intersection and degree conditions,
unchanged segment labels and representatives, and projected short-spacing
vertex counts. The proof obligation is preservation of the geometric
compiler premises, not another source-coloring solver run. Experience:
round 045 shows unused spatial extent remains; rank compaction changes that
premise without changing any network constraint.

## Evidence and diagnosis

All six networks preserve the checked geometric premises. Source constraints
and representative IDs are unchanged, so round 045 decision/recovery evidence
is reused. [output.jsonl](output.jsonl) reports projected targets from 834,081
vertices for the smallest nonempty case to 6,304,939 for the largest.
Command: `python3 rounds/046/probe.py` from the campaign directory. Zero solver
queries, repairs or reruns. The monotone-map argument holds for arbitrary
orthogonal input networks: intersection is a conjunction of coordinate-order
and equality predicates, all preserved by strict rank maps.
Experience extraction: pending geometric-composition update for coordinate
rank compaction; campaign-only writes block the shared destination.
Next: test bent-wire length compensation, a different way to reduce spacing.
