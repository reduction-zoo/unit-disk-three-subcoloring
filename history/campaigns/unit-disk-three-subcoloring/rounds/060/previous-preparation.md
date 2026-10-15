# Testing foundation

Z3 5.1.0 supplies exact Boolean SAT and integer color-domain oracles. Source
clauses become disjunctions. For each induced P3, the target encoding forbids
all three colors being equal. These constraints are necessary and sufficient:
a graph is a disjoint union of cliques exactly when it has no induced P3.
Only SAT and UNSAT are accepted; other statuses raise an error. No timeout.
Witness validation separately checks monochromatic components for completeness.
Geometry uses Python Fraction with exact squared distances.

Run from the repository root:
`python3 campaigns/unit-disk-three-subcoloring/work/check.py --self-test`.
The [raw result](evidence/preparation/self-test.json) records 228 comparisons
of the Z3 graph oracle with exhaustive coloring enumeration, over every labeled
simple graph on zero through four vertices and k in {1,2,3}; six source cases
include four YES and two NO cases. Boundary geometry, three malformed targets,
and two deliberately wrong rule/recovery pairs are rejected as appropriate.
BC4 is an abstract 15-vertex NO instance for three-subcoloring and a YES instance
for four colors; it is not claimed to be unit disk. At initial preparation, a valid rational geometric NO fixture was missing.
Round 008 subsequently supplied a 34-vertex critical grid subgraph, independently
encoded with Boolean indicators and integer geometry. The current self-test
checks it is NO for three colors and YES for four; see
[updated raw result](evidence/preparation/geometric-no-self-test.json). The original
self-test output is retained. This repair adds coverage without changing either
oracle or any expected source decision.

The candidate harness runs the actual forward process, solves its output,
compares decisions, invokes extraction in a fresh process on solver witnesses,
and checks source satisfaction. It exhausts witnesses for targets with at most
six vertices and checks up to six witnesses otherwise. No candidate or recovery
has been tested yet. No reduction correctness is implied by oracle tests.

The source witness now uses sparse assignment dictionaries, false by default,
as defined in [contract.md](contract.md). Source oracles allocate only mentioned
variables. This preserves the decision language and fixes the output-size
obligation for compressed declarations. [Round 028](../rounds/028/round.md)
preserves the dense contract and supplies the current self-test and 5,001-digit
declaration regression. Geometry and target expectations are unchanged.

The current full-source harness accepts `--case NAME` to select a declared
prepared case. An unknown name fails explicitly. Only `--case empty` has been
run against the integrated candidate; all other full-source cases remain
unverified. [Round 040](../rounds/040/round.md) records the current self-test
and exact projected output sizes that prevent a dense full-suite run.
