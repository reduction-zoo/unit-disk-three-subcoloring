# Round 006 — Polynomial witness size for compressed variable declarations

## Plan

Investigate and repair the encoding obligation found in round 005. The JSON
integer n can be exponentially larger than its own bit length; for an empty
formula, a length-n Boolean output is not polynomial. Preserve the old contract,
extractor and validators, then use a sparse assignment dictionary with false
as the default for omitted variables. This represents the same source solution,
with no change to the source decision language, target or graph construction.
Make source oracles allocate only mentioned variables. Scope: the five prepared
cases and nine extended cases, including n=10^30 with no clauses and with a
three-distinct-literal clause. Both maps, general bit bounds and exact checks
must pass before independent review. Experience retrieval found no applicable
compressed-variable or unused-variable entry; sparse Schur-matrix interfaces
have different premises. Completion: polynomial encoding argument and executable
large-label tests, or a concrete remaining defect.

## Evidence and diagnosis

The forward graph map is unchanged. Recovery and source validators now use
sparse dictionaries; variable IDs and rational endpoints are explicitly encoded,
so no numeric magnitude becomes a loop bound. The old encoding convention was
the cause of the polynomial-bound gap, not the graph construction.

Commands from the repository root:
`python3 campaigns/depth-three-unit-two-interval/work/check.py --candidate campaigns/depth-three-unit-two-interval/work/algorithm.py` and the analogous
`work/verify.py` command. [Prepared](prepared.jsonl): five source cases, six
recoveries. [Extended](verification.jsonl): nine source cases, fourteen recoveries,
including n=10^30. [Large encoding](large-encoding.jsonl): a 5,001-digit n,
empty target, one successful recovery with an 18-byte source witness. Four
invalid sparse assignments were rejected; [fault injection](fault-check.jsonl)
rejected all three wrong programs. [Rational encoding](rational-encoding.jsonl)
rejects compressed exponent notation and accepts explicit fractions.

Source self-test [passed](self-test.jsonl). Target rational parsing and Python's
integer-string digit limit were then tightened for the stated explicit-rational
and unbounded-integer contracts; those changes preserve all accepted test inputs.
No full-instance rerun is needed for these grammar/configuration-only changes;
new grammar and large-integer regressions cover the affected inputs. Internal
solver query counts and aggregate time/token totals are unavailable.

**Experience extraction:** created [compressed variable declarations](../../../../research/experience/compressed-variable-declarations.md).
The complete rule is ready for independent review; correctness and novelty
remain provisional. Short-term prospects high, uncalibrated, conditional on
review of the central-deletion proof and literature coverage.

## Next action

Request independent review of the complete candidate and both maps.
