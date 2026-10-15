# Round 042 — wider-span wire composition

## Plan

Use round 041's exact primitive scale interval to test pair composition at
lengths 50q,51q,52q,53q. Evaluate all 16 length pairs and all 16 state pairs
from states {0,1,4,5}: 256 motifs. These include the forward/reverse geometry
and the two internal color permutations used beside inequality cells.
Reuse the original dense graph and independent clique-component validator.
Completion: record induced-copy preservation and clean global validity for
every motif. If failures occur, retain the exact length/state counterexample;
do not infer that every witness fails. Experience: pending geometric
composition finding; new premise is the expanded scale interval.

## Evidence and diagnosis

[output.jsonl](output.jsonl): 256 pair motifs, all preserve induced
copies and pass the clean witness checker. Command: `python3 rounds/042/probe.py`
from the campaign directory. Zero solver queries, repairs or reruns.
Experience extraction: this extends the pending geometric-composition entry;
shared writes remain outside campaign scope. Finite canonical witness evidence
supports the wider-span chain, not universal recovery by itself.
Next: check the inequality connector over the same wider lengths.
