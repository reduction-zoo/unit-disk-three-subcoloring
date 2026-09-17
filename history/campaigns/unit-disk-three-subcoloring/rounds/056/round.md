# Round 056 — broaden complete source injection

## Plan

Run the actual compact forward command on the remaining nonempty prepared
sources: tautology, forced conflict and the three-variable formula. Reuse the
unchanged positive-unit and opposite-unit target evidence. Independently
brute-force each source, check all manifest-induced graphs on its actual
output, and require either a necessary-projection NO certificate or a globally
validated solver-derived YES witness. Search each YES case for at most 64
phase assignments, and check six fresh-process recoveries. Check the empty
source directly. The larger scope tests interacting clauses and multiple
variables, not just the unit-formula construction branch. The certificate
producer remains untrusted and separate from the decision/recovery checks.
Completion: all three full cases and the empty case, or a saved mismatch or
explicit unknown. Experience: reuse rounds 052--055's checked oracle premises.

## Evidence and diagnosis

All four declared cases pass. Tautology: 889,976 vertices, two phase queries
and six recoveries. Forced conflict: 3,569,708 vertices and projection UNSAT.
Three-variable formula: 4,059,987 vertices, 26,403,979 exact edges, two phase
queries and six recoveries. Empty: zero vertices and six recoveries. Together
with unchanged rounds 053/054 evidence, all six prepared source decisions
agree (four YES, two NO), with 24 independent-witness recovery calls total.
Command: `python3 rounds/056/probe.py` from the campaign directory;
[output.jsonl](output.jsonl). This round used two base CP-SAT queries, three
projection CP-SAT queries and four Z3 phase queries, plus brute-force source
checks. No repairs or reruns. Large targets were actually emitted and checked.
Experience extraction: pending projection entry now has multi-clause and
multi-variable use evidence; it enabled successful finite validation without
assuming a global composition lemma. This does not measure general research
yield or prove arbitrary-input correctness. Shared writes remain blocked.
Next: close the specific middle-unit gap in the all-length wire argument.
