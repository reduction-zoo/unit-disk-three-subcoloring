# Round 051 — integrate the compact geometric compiler

## Plan

Compose incident-range buses, strict coordinate-rank compaction and the 334q
detour into solver-free forward/recovery commands. Preserve the prior current
candidate before replacing it. Emit the smallest prepared nonempty source
through a fresh process. Independently validate its actual point count and
compare against a separately generated candidate witness/geometry fixture;
then check the entire witness against actual rational distances with the
existing sparse target predicate. This initial witness comes from the
candidate's extension, not an independent target solver; report that limit.
Recover under all six global color permutations in fresh subprocesses and
validate source assignments independently. Completion: one full nonempty
source execution with six recoveries or a concrete saved failure.
Experience: compressed-variable declarations still require sparse recovery;
rounds 045--050 support only the stated compiler changes, not this full test.

## Evidence and diagnosis

The fresh forward process produced [target.json](target.json), 537,397 vertices
and 15,813 primitive copies. Its actual coordinates match the separately
built fixture exactly. The full sparse witness check passes, and all six
fresh-process recovery calls return a satisfying assignment. See
[output.jsonl](output.jsonl); commands are `python3 work/algorithm.py <
rounds/051/source.json > rounds/051/target.json` and `python3
rounds/051/probe.py > rounds/051/output.jsonl` from the campaign directory.
Zero solver queries, repairs or reruns. This is the first nonempty full-source
witness test, but the witness is candidate-generated. It is not an independent
target-solver pass, and no full-source NO output has yet been certified.
Experience extraction: pending composition entry records this exact evidence
boundary; shared writes remain blocked. Next: test a certificate-assisted
partial target oracle using checked local necessary relations for NO and
independently searched, globally validated colorings for YES.
