# Round 023 — common coordinates and strict geometric margins

## Plan

Hypothesis: all successful equality motifs survive the same rational map
p -> (L dot(p,D)/|D|^2, L cross(D,p)/|D|^2), L=3969/1000, so they share the
connector's axis-aligned step. Check all 64 two-copy state pairs, the junction,
and both saved extended junctions after this map. Check local equality adjacency
and all saved canonical colorings/cleanliness. The connector is already in this
frame and is retained unchanged. Scope: 68 finite motifs, no solver queries.

Across these motifs, compute exact minimum nonedge squared distance and maximum
edge squared distance. Choose one rational global shrink that preserves every
edge/nonedge, makes inequalities strict, and retains the distance-two separation
bound for remote arms. Derive an explicit rational coordinate-perturbation margin
from the finite squared-distance margins. These bounds would support small
uniform wire length adjustments in a general layout proof; they do not create
that proof automatically. Use rounds 018/021's local-to-global separation and
round 022's scale diagnosis. No timeout.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/023/probe.py`.
[Output](output.jsonl): all 68 motifs retain valid clean witnesses; normalized
wire/junction graphs retain their original adjacency. The connector was checked
in its existing frame. [Exact margins](margins.json) give minimum nonedge squared
distance 204788493/197000000 and maximum edge squared distance
15752961/15760000. A rational global shrink makes all comparisons strict and
retains the remote-arm distance-two bound. No solver queries or reruns.

For coordinate perturbations of magnitude at most epsilon in each coordinate,
any pair's squared-distance change is at most (4H+8)epsilon when epsilon<=1,
where H bounds its original L1 difference. The saved epsilon leaves at least
half the computed squared margin. This is a conservative robustness certificate
for these motifs, not yet a scalable routing algorithm.

Supporting source search located the primary Garey--Johnson--Stockmeyer (1976)
paper, https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/JohnsonDavid2.pdf,
for the known 3-coloring planarization composition. Queries on 2026-09-16:
`Garey Johnson Stockmeyer 1976 planar 3 coloring crossover gadget pdf` and
`planar 3 coloring crossover gadget 13 vertices reduction SAT pdf`. Its exact
construction and extraction still need inspection before use.

Experience extraction: update the pending composition finding with common-frame
normalization and strict rational margins. Robustness is local to the checked
motifs; it does not prove arbitrary layouts. Shared proposal remains pending.

## Next action

Avoid relying on very small continuous length adjustments in the executable
layout. Test two commensurate rational wire lengths and an integer-multiple
inequality span. A finite mixed-length interaction table could give exact
integer routing with a simple coin identity and moderate constant-size cells.
