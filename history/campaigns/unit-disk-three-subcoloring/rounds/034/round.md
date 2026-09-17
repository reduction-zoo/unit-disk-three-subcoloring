# Round 034 — complete geometric crossover expansion

## Plan

Expand all 44 paths of the fixed round 032 crossover, putting junctions at
network vertices and bends. On an inequality path, put its unique inequality
in the first straight segment; all subsequent segments carry the second
endpoint color. Check two canonical boundary relations (same/same and
different/different), using saved valid mixed-network witnesses. Their color
permutations cover all nine allowable crossing assignments. Validate the actual
expanded coordinates and every local induced primitive. This finite scope is
two complete macro witnesses, zero solver queries. Reuse round 033's checker
and routing constructor. Full source composition remains outside this round.

## Evidence and diagnosis

Both complete 409,345-vertex geometric crossover witnesses pass. Each contains
12,040 local copies, all with exactly the intended induced adjacency.
[output.jsonl](output.jsonl) records both full checks; [crossover.json](crossover.json)
and two witness files preserve the actual geometry. Command: `python3
campaigns/unit-disk-three-subcoloring/rounds/034/probe.py`. Zero solver queries,
source injections or recovery calls. No repairs; time/token unavailable.

The macro is large but constant. Its coordinates are independent of boundary
colors: only witness permutations change. This supports a geometric crossover,
conditional on the two finite base forcing lemmas and a general routing proof.
It does not by itself establish a complete Karp map.
Experience extraction: extend pending geometric-composition with the complete
macro evidence and the distinction between constant template verification and
source-level verification. Shared destination remains restricted.
Next cross-check base forcing with a separately implemented mature solver.
