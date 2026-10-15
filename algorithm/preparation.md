# Testing foundation

The source language is 3-SAT with a binary variable-count declaration and
sparse assignment witnesses. The target language is three-subcolorability of
an explicitly listed rational unit disk representation. The exact formats
and malformed-input convention are in [contract.md](contract.md).

## Small exact oracles

`check.py --self-test` uses Z3 for source formulas and explicit induced-P3
constraints for small target graphs. A separately written monochromatic
component predicate checks that every component is a clique. The retained
[current self-test](../history/campaigns/unit-disk-three-subcoloring/rounds/060/integrated-self-test.json) covers 228 graph
oracle comparisons, six source cases, a rational geometric NO fixture,
malformed targets and intentionally incorrect decision/recovery pairs.
Original preparation evidence remains under `work/evidence/preparation/`.

## Complete-source certificate oracle

The actual full-source outputs are too large for the original dense target
solver. The candidate harness now uses the certificate-assisted partial oracle
from rounds 052 and 053. A separate, untrusted certificate producer supplies
primitive index lists. The oracle independently computes each listed induced
graph from the actual emitted centers. CP-SAT proves the forbidden terminal
relations of the two fixed primitive graphs and solves the resulting necessary
terminal constraints. Projection UNSAT is a conclusive target NO certificate;
projection SAT is not a target decision.

For a SAT projection, Z3 searches permutations of independently validated
local clean colorings. The actual whole graph supplies monochromatic P3
counterexamples. A complete coloring is accepted only when all monochromatic
components are cliques in that graph. The search has a finite scope of 64
phase assignments. Restricted-domain UNSAT or exhausted scope raises an
explicit unknown error; neither is accepted as target NO.

Exact integer-scaled coordinates feed a SciPy Chebyshev neighbor query, followed
by an integer Euclidean-distance filter. Coordinates must be strictly smaller
than 2^51 in magnitude after scaling, and squared-distance products must fit
int64. The range check occurs in Python integers before conversion. Empty and
malformed encodings are checked explicitly. Unsupported numeric ranges fail;
no complete arbitrary-rational target solver is claimed. Versions are recorded
in [versions.json](../history/campaigns/unit-disk-three-subcoloring/rounds/060/versions.json).

The new predicates pass [516 geometric and 5,422 coloring comparisons](../history/campaigns/unit-disk-three-subcoloring/rounds/055/output.jsonl),
seven malformed cases, the empty target and [four numeric-bound cases](../history/campaigns/unit-disk-three-subcoloring/rounds/055/numeric-output.jsonl).
The incomplete-manifest failure and repair in round 054 test the distinction
between missing evidence and a false reduction. The initial failed phase
assignments in round 053 are actual whole-graph witness failures, repaired by
excluded-assignment clauses rather than weakened predicates.

## Injected-instance commands

`check.py --candidate PATH` executes every prepared source through the actual
forward subprocess, runs the certificate oracle on its actual output, checks
YES/NO agreement with the independent Z3 source solver, and validates recovered
source assignments in fresh processes. It checks six color permutations of
one independently found witness for each nonempty YES target, and the single
empty witness for an empty target. `--case NAME` selects one explicit case;
an unknown name fails. `--evidence DIR` selects a new directory and refuses to
overwrite prior evidence.

`verify.py --candidate PATH` independently brute-forces the active variables
of additional sources with 5,001-digit variable declarations and labels. It
checks both a valid YES and valid NO input, sparse recovery, empty formulas
and six malformed source encodings. It does not import `check.py` or the
candidate. The two harnesses share the large-target oracle, so their passes
are not independent implementations of that oracle. The small exhaustive
checks and required native reviewer provide separate scrutiny.

All documentation and evidence distinguish finite test coverage from the
general proof. Current candidate results are recorded in [verification.md](verification.md).
