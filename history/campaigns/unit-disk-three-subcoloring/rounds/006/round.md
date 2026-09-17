# Round 006 — published wire geometry audit

## Plan

Hypothesis: the co-comparability three-color reduction's palette is its only
unit-disk obstacle, so a palette replacement would suffice. Inspect its local
false-twin wire for an induced K2,3 and verify the geometric exclusion in a
primary source. Scope: the five vertices l_i,l'_i,l_j,l'_j,c_i for i != j,
Section 4.3 of arXiv:2506.19452v1, and the planar half-lens argument. Test the
induced adjacency explicitly; no coordinate synthesis if the obstruction holds.

Prior evidence: rounds 003--004 already reject the K4,4,4 palette and complete
independent replication. The new question concerns the remaining wire with
that palette removed. Shared experience has no applicable wire result; use
local obstruction records without importing matching-cut assumptions.

## Evidence and diagnosis

The five listed vertices induce K2,3: the nonadjacent pair l_i,l'_i is completely
joined to the independent triple l_j,l'_j,c_i. This follows directly from the
false-twin and matching adjacencies in Section 4.3, construction items 2--3.
The check `python3 campaigns/unit-disk-three-subcoloring/rounds/006/probe.py`
records those six edges in [output](output.jsonl). One structural template,
no solver query, source injection, or recovery call.

The primary geometric source [Optimization in Geometric Graphs](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/a8138e97-e807-4924-800e-40c4bf8a64b5/content),
printed page 19, Lemma 4, proves K2,3 and K1,6 cannot be induced in unit disk
graphs. The K2,3 argument places three independent common neighbors in the lens
of two nonadjacent centers and uses the two half-lenses. Also see
[da Fonseca et al., January 2014 manuscript](https://pageperso.lis-lab.fr/guilherme.fonseca/domudg.pdf),
which uses this forbidden graph. Queries on 2026-09-16:
`"unit disk" "K2,3" forbidden`, `"unit disk graphs" "common neighbors" "nonadjacent"`,
and `"unit disk graph" "K_{2,3}"`. A Liverpool PDF returned HTTP 406; the above
primary PDFs were accessible. This is a known geometric exclusion, not discovery.

Conclusion: even with its palette removed, the published false-twin wire is
not unit disk as soon as two such bags and one matched core vertex exist.
A palette-only replacement cannot implement this construction. No judgment is
made about other graph classes or about the correctness of the published rule.
No repair/rerun; usage unavailable.

Experience extraction: pending proposed entry
`research/experience/unit-disk-false-twin-wire-obstruction.md`. Exact premise:
two independent twin pairs completely joined, plus a vertex adjacent to one
pair and neither member of the other. Consequence: the five vertices induce
K2,3, excluding unit-disk realizability. Evidence: published exclusion and this
adjacency audit. Main-agent application, not independently reviewed. Shared
write remains outside the user-supplied campaign scope.

## Next action

Check whether the previous geometric YES results are a boundary effect by
trying three larger regular instances, then use any NO instance as a critical
constraint source. This is a diagnostic threshold check, not a claim that
larger random sampling alone can discover a reduction. Both palette and wire
must now be native geometric constructions. Short-term prospects: low,
uncalibrated; a geometric obstruction or forced relation would change that.
