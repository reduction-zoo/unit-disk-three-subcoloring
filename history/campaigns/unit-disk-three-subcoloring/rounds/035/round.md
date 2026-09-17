# Round 035 — independent solver encoding of primitive forcing

## Plan

Re-encode the two 35-vertex base gadgets directly in OR-Tools CP-SAT, using
integer-scaled rational geometry and forbidden monochromatic induced P3s.
For each gadget solve its equal and unequal pinned terminal patterns, and
the clean extension of its allowed pattern: six queries. Do not import the
Z3 oracle, geometric constructor or saved candidate witnesses. This addresses
common-solver dependence, not author independence or a full-rule review.
The exact source target is unchanged. Reuse the base coordinates only.
Experience: computational base evidence remains separate from general routing
proof and source recovery; no existing shared claim supplies these lemmas.

## Evidence and diagnosis

All six CP-SAT queries agree with the intended primitive relations: two
forbidden patterns INFEASIBLE, four allowed/clean patterns OPTIMAL. Coordinates
and P3s were reconstructed without importing Z3 or the candidate. Counts and
witnesses appear in [output.jsonl](output.jsonl), reproduced by `python3
campaigns/unit-disk-three-subcoloring/rounds/035/probe.py`. No source injections,
recovery calls or repairs; time/token unavailable.

This removes the earlier common-solver limitation for these finite relations.
It remains main-author computational evidence, not independent author review
or a standalone proof certificate. Experience extraction: extend pending
base-gadget/composition evidence with this second solver result; shared files
remain unchanged. Next implement the full planar crossbar at the intermediate
constraint level and test its source recovery.
