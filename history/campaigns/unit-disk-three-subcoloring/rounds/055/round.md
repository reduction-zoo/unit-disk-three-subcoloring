# Round 055 — falsify the certificate oracle's assumptions

## Plan

Check the Chebyshev-neighbor/Euclidean-filter graph against independent
all-pairs integer arithmetic on every subset of a 3-by-3 half-unit grid,
plus three two-point cases at distance 1-1/S,1,1+1/S with S=39400000 and a
large exactly representable translation. Check the monochromatic-component
clique criterion against direct induced-P3 enumeration for every labeled
graph on at most four vertices and every three-color assignment. Check
empty targets and five malformed encodings. Preserve any checker defect
before repair; do not change expected source answers. These finite exhaustive
checks challenge numerical boundaries, duplicate/empty behavior and the
logical witness predicate used in the new full-target verification strategy.
Completion: all stated comparisons and fault checks, with actual counts.
Experience: round 054 distinguishes a producer omission from an oracle error.

## Oracle repair

Inspection found that empty dict/string values for `centers` could pass the
new parser's empty iteration. Require a list explicitly, and add both cases
to the five planned malformed regressions. Preserve the initial successful
five-case log as `initial-output.jsonl`. The earlier empty-array shape repair
was also identified by inspection, not by an invented failed execution.
Rerun the same finite geometric and witness checks after the parser repair.

## Evidence and diagnosis

The repaired run passes 516 exact geometric graph comparisons, 5,422
coloring-predicate comparisons, the empty target and seven malformed cases.
See [output.jsonl](output.jsonl); command `python3 rounds/055/probe.py` from
the campaign directory. Zero solver queries; two parser/empty-array defects
were repaired, with one full rerun. No candidate change was needed.
The integer Chebyshev query is used only with exactly representable bounded
integers, and the final Euclidean filter uses checked int64 squared bounds.
This finite-domain implementation rejects unsupported numeric ranges; it is
not claimed as a complete oracle for arbitrary binary-rational encodings.
Experience extraction: pending projection entry gains the numeric-domain and
empty-encoding premises. Shared writes remain blocked.
Next: extend actual full-source coverage to the remaining prepared formulas.

## Later numeric-bound audit (2026-09-16)

A follow-up code audit found that applying NumPy absolute value before the
range check could overflow for int64 minimum. Check Python integers before
conversion instead, preserving the previous code as
`before-integer-bound-repair.py`. Four explicit domain-bound regressions are
in `numeric_probe.py` and `numeric-output.jsonl`. This corrects unsupported-input
handling; all emitted campaign coordinates were already strictly inside the
bound, so prior nonempty graph decisions do not change. No failed research
candidate or new round is inferred from this oracle implementation repair.
