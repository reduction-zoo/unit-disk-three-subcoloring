# Round 054 — full-source NO certificate

## Plan

Emit the opposite-unit formula through the current forward subprocess.
Generate an untrusted list of primitive index sets by instrumenting the
coordinate emitter; it is a certificate producer, not an oracle. Independently
check every listed induced graph against the base graphs and solve its
necessary terminal projection. Require conclusive projection UNSAT and an
independent brute-force source NO decision. No target witness is expected.
Scope: one source formula with clauses (x,x,x) and (-x,-x,-x), two base-graph
queries and one projection query. Reject malformed/corrupt certificates; a
certificate-generation assertion does not establish any target property.
Experience: round 052's necessary projection supports NO independently of
cross-copy edges and of the global composition lemma.

## Repair during execution

The first run ended at the expected-NO assertion: its projection was SAT.
Inspection found a certificate-producer transcription defect: inequality
primitives were emitted but never appended to the manifest. The projection
oracle correctly returned unknown, not YES. The candidate and target are
unchanged. Preserve `incomplete-certificate_emitter.py`, `incomplete-copies.json`
and `incomplete-output.jsonl`; repair only the certificate producer and rerun
against the same actual target. This is one implementation repair within the
round, not a new research attempt or a reduction counterexample.

## Evidence and diagnosis

After the certificate-producer repair, all 45,546 induced primitive graphs
match the actual 1,547,820-vertex target, and its 490-class projection is
CP-SAT INFEASIBLE. The independently checked source is NO. See
[output.jsonl](output.jsonl). The target was generated once; certificate
production/projection ran twice. Six solver queries total across the failed
and repaired runs. No candidate code or target data changed during repair.
Experience extraction: extend pending induced-relation-projection: an
incomplete manifest can lose NO-detection power while remaining logically
sound; SAT must remain unknown. The missing inequality regression and raw
failed evidence are retained. Shared writes remain blocked.
Next: check the new oracle's exact graph and global witness predicates against
small exhaustive definitions before broadening source coverage.
