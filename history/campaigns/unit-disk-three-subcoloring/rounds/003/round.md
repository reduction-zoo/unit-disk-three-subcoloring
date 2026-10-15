# Round 003 — independent replication of proper-color vertices

## Plan

Hypothesis: replace each vertex of a proper-three-coloring source by four
independent twins, joining neighboring bags completely. A repeated color in
each bag could recover a proper source color. Check the semantic equivalence
as a general lemma, then check whether even one expanded source edge is a
unit disk graph. Scope: this single replacement family, source graphs with at
most four vertices for finite semantic checks, and the induced K3,3 obstruction.
No geometric synthesis is warranted if one edge already violates the class.

Relation to prior evidence: changes from fixed-grid palette forcing to direct
witness decoding. Shared experience search has no applicable subcoloring entry;
round 001's geometric validation requirement is retained.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/003/probe.py`.
[Output](output.jsonl) records 76 source graphs, 76 target queries, and validated
repeated-color recovery for each SAT result. These are proper-coloring helper
instances, not injected 3-SAT instances. No complete-rule recovery calls.

General semantic proof: four independent twins contain a repeated color under
three colors. No neighboring bag can use that color, since two twins and that
neighbor would form a monochromatic P3. Choosing a repeated color per bag
therefore yields a proper coloring. Conversely, color each bag monochromatically
from a proper coloring. This is a valid generic reduction, not a novelty claim.
Geometry fails on any edge: the output contains an induced K3,3. Triangle-free
unit disk graphs are planar (primary source: Marin--Watrigant 2025, full version
Section 4.1), whereas K3,3 is not planar. Hence the family cannot meet the fixed
target restrictions even on source YES instances. No rerun; usage unavailable.

A supporting read of the same paper, Section 4.3, found its three-color palette
uses K4,4,4 (Lemma 16), so the published palette has exactly this obstruction.
Primary URL: https://arxiv.org/html/2506.19452v1 ; checked 2026-09-16.

Experience extraction: pending proposed entry
`research/experience/independent-replication-unit-disk-obstruction.md`.
Premises: complete joins between independent replicated bags; at least three
vertices in each of two adjacent bags. Consequence: induced K3,3 excludes any
unit disk representation. At four replicas, logical repeated-color decoding
works but geometry cannot. Main-agent proof and 76 finite checks; no independent
review. Shared destination is outside the user-supplied campaign write scope.

## Next action

Investigate whether smaller or adjacent replicas avoid the obstruction while
retaining logical force. This is a targeted repair of the replication premise,
not a fresh source encoding. Check explicit K4 counterexamples and the general
true-twin invariance lemma before pursuing any geometric representation.
