# Round 052 — certified local projection of the actual target

## Plan

The full graph has hundreds of thousands of vertices, while its constraints
repeat two 35-vertex primitives. Treat a supplied primitive-index manifest as
untrusted. Independently compute each listed induced graph from the actual
emitted rational coordinates and compare it with the two independently solved
base graphs. Project their necessary terminal equality/inequality relations,
then solve that constraint graph. Projection UNSAT proves target NO because
restriction to induced subgraphs preserves subcolorability. Projection SAT
is only inconclusive until a complete target coloring passes a global check.
First scope: the actual round 051 target and all 15,813 listed primitives;
two base-graph forbidden-relation solver queries and one projection query.
Deliberately corrupt one manifest's vertex index to confirm rejection.
This is a new verification proof strategy, not a candidate correctness claim.
Experience: no applicable shared certificate oracle was found; do not assume
a candidate's composition lemma or trust its manifest. Completion: checked
projection and explicit SAT/NO/unknown semantics, with raw outputs retained.

## Evidence and diagnosis

Both forbidden primitive relations are CP-SAT INFEASIBLE. All 15,813
manifest copies match independently computed induced graphs of the actual
537,397-vertex target. Their projection has 165 terminal classes and is SAT;
this is explicitly an unknown target decision. The corrupted manifest is
rejected. Three solver queries, no repairs or reruns. Command: `python3
rounds/052/project.py` from the campaign directory; [output.jsonl](output.jsonl).
Experience extraction: proposed pending `research/experience/induced-relation-projection.md`.
Checked necessary projections certify NO only when UNSAT; SAT needs a full
witness. This is an author-checked general logical implication, not a new
hardness theorem. Shared writes remain blocked by campaign scope.
Next: independently search internal color permutations and check whole-target
clique components, using counterexamples to constrain subsequent assignments.
