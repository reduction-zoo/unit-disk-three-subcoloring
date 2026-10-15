# Round 039 — independent actual-target YES/NO geometry tests

## Plan

Inject two four-edge rectangular networks through the witness-independent
geometric map: all equalities (YES), and three equalities plus one inequality
(NO). Independently rebuild exact adjacency from emitted rationals using
integer spatial buckets, derive P3 constraints, and solve with CP-SAT. Check
returned YES colorings directly and read their central port colors to recover
the network assignment. No primitive metadata or abstract-relation shortcut
may replace the actual target constraints. Scope: two target decision queries
and six color-permuted network recoveries for the YES case. These are network
injections, not full 3-SAT injections. One solver worker avoids parallel search
replicas; no timeout or query-time bound. Reuse source-independent construction
and the mature-solver testing policy.

## Evidence and diagnosis

Independent CP-SAT solving of the actual geometric outputs returns OPTIMAL
for the equality rectangle and INFEASIBLE for the inconsistent rectangle.
The YES witness passes direct geometric validation and all six network
recoveries. [output.jsonl](output.jsonl) records vertex, P3, branch and conflict
counts. Commands: `python3 .../rounds/039/prepare.py`, then
`python3 .../rounds/039/probe.py`, where `...` is the campaign directory.
Counts: two actual geometric network injections, two target queries, six
network recoveries, zero complete 3-SAT geometric injections. No repairs;
aggregate time/token unavailable.

These checks exercise both directions without relying on primitive metadata
or a predicted abstract target answer. They do not test the enormous complete
source crossbar. Experience extraction: extend pending geometric-composition
with actual-target evidence and the remaining coverage gap. Shared destination
restricted. Next integrate both source maps and quantify full-test size before
claiming that the pipeline has completed verification.
