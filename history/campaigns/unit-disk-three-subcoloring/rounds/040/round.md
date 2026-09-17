# Round 040 — complete map integration and verification feasibility

## Plan

Compose the source compiler, planar network and witness-independent geometric
emitter into a deterministic streaming forward command. Recover sparse source
assignments from central bus colors, recomputing deterministic hub indices.
Prove polynomial size in the actual encoded source, including compressed
variable declarations. Test both command modes on two empty-clause sources
(including a large declaration) and six malformed inputs. Check the exact
vertex-count formula against saved macro/rectangle sizes, then apply it to all
six prepared cases. The complete-source test sizes determine whether the
current independent harness can run; do not hide an untested nontrivial branch
behind passing empty cases. No new construction family beyond the existing
composition is introduced. This is the final authorized discovery round.
Experience: use compressed-variable-declarations and the recorded geometric
composition results; record remaining resource and evidence gaps explicitly.

## Evidence and diagnosis

Both command modes pass two empty-clause source instances, including a
5,001-digit declaration with an 18-byte sparse recovery. Six malformed inputs
map to null. The exact size and hub-index formulas match saved geometry.
The selected `--case empty` harness pass and complete oracle self-test are
recorded separately. The case selector only limits an explicit test scope; it
does not change expected answers or claim coverage of skipped cases. The prior
checker is preserved. Commands and outputs:

- `python3 .../rounds/040/probe.py`: [output.jsonl](output.jsonl).
- `python3 .../rounds/040/count_check.py`: [count-check.jsonl](count-check.jsonl).
- `python3 .../work/check.py --candidate .../work/algorithm.py --case empty`:
  [harness-empty.jsonl](harness-empty.jsonl).
- `python3 .../work/check.py --self-test`: [self-test.json](self-test.json).

Here `...` denotes `campaigns/unit-disk-three-subcoloring` from the repository
root. The complete source tests use four decision queries, and the selected
harness adds one target query; oracle self-test queries are excluded. There
are three empty-source executions/recoveries including the repeated harness
case, six malformed forward calls, and zero nonempty full-source injections.
Aggregate time/token usage unavailable.

The initial proof wording incorrectly said that a cell boundary contained only
ports. Inspection shows north/east boundary segments. The actual construction
has south/west padding, so the relevant premise is legal pairwise gluing.
[seam_check.py](seam_check.py) checks all 64 adjacent/diagonal cell-type pairs;
[seam-check.json](seam-check.json) confirms noncrossing and maximum degree four.
This repairs the proof description without changing coordinates or the rule.

The smallest prepared nonempty target has 19,324,556 vertices; the largest has
136,799,574. These are exact projected counts, not generated files. A dense
adjacency matrix for even the first would exceed this machine's 16-GiB memory
by orders of magnitude. The complete prepared source suite was therefore not
run. No OOM, timeout, or full-suite success is claimed. Actual independent
geometric solving remains limited to the round 039 networks.

Experience extraction: extend pending geometric-composition with the exact
size formulas, explicit test-coverage limit, and corrected cell-gluing premise.
The compressed-variable entry also has a pending use update. Five proposed
new entries and one existing-entry update remain blocked by campaign-only
writes; zero shared files were created or updated.

## Decision

Forty rounds are complete and the allocation is exhausted. Stop discovery
with an implemented candidate and an unreviewed general argument, not a
qualifying result. Do not request the success-path independent reviewer before
full-rule checks pass. Near-term completion prospects are unknown (uncalibrated):
local correctness evidence improved, but full nonempty source verification is
not currently executable with the existing dense harness and output sizes.
A useful next allocation must address practical independent full-target
verification or a much smaller source layout, not repeat the same local tests.
