# Campaign state

Status: **ready_for_expert_review**. The additional allocation finished on
2026-09-16: **60 started, 60 completed; zero remaining**. Rounds 041--060
are the 20 new research attempts; subsequent verification and writing added
no research rounds.

The [complete rule](work/algorithm.py) reduces 3-SAT to three-subcoloring of
rational unit disk graphs and recovers a source assignment from every valid
target coloring. Its incident-range buses, coordinate compaction and rational
detours give quadratic vertex count and logarithmic coordinate bit length.
The [8-page English paper](work/manuscript.pdf) includes the general
computer-assisted proof, three structural vector figures and reproduction
instructions. The [Typst source](work/manuscript.typ) compiles successfully;
every initial page and all pages affected by repairs were visually inspected.

Both integrated suites pass: [prepared](rounds/060/prepared-suite.jsonl) and
[additional](rounds/060/additional-verification.jsonl). These exercise actual
YES/NO outputs, including a 4,059,987-vertex target and 5,001-digit source
labels. The partial oracle certifies NO through checked necessary constraints
and YES only through a globally valid coloring; restricted search failure is
unknown. The two suites share this oracle. See [verification](work/verification.md).

The native independent [review](reviews/compact-construction/review.md) gives
**advance**, with independent primitive, routing, clause and locality checks.
The [manuscript addendum](reviews/compact-construction/manuscript-addendum.md)
retains that decision; its squared-span wording correction has been applied.
No algorithm or test changed after review. A development-proof snapshot is
preserved in round 060; its current status points to the manuscript's reviewed
locality elaboration.

Correctness is supported as a computer-assisted general proof, not inferred
from test pass counts. Finite forcing still trusts mature solvers without
formal UNSAT traces. Novelty is supported within the recorded primary-literature
coverage; full WLAN-paper theorem coverage and exhaustive priority remain open.
Significance is a moderate geometric-graph complexity contribution if expert
assessment confirms the result. Further discovery rounds are not recommended
for this completed construction; the next step is human expert assessment.
No publication or production-library integration has occurred.

## Round index

| Round | Mechanism | Actual result |
|---|---|---|
| [001](rounds/001/round.md) | Initial grid pair forcing | 240 SAT queries; no pair forcing on any induced subset |
| [002](rounds/002/round.md) | Grid NO baseline | 12 grids all SAT |
| [003](rounds/003/round.md) | Independent replication | 76 semantic checks; output geometry fails |
| [004](rounds/004/round.md) | Replication repair | Four queries plus true-twin lemma exclude proposed variants |
| [005](rounds/005/round.md) | Irregular geometric hosts | 96 samples all SAT |
| [006](rounds/006/round.md) | Published wire audit | Induced K2,3 persists without palette |
| [007](rounds/007/round.md) | Larger grid threshold | First query finds 49-vertex geometric NO |
| [008](rounds/008/round.md) | Independent encoding and deletion | 51 queries; 34-vertex critical obstruction |
| [009](rounds/009/round.md) | Critical boundary relations | 224 queries; 76 forced pair relations |
| [010](rounds/010/round.md) | Clean pair composition | All 76 clean-pair queries UNSAT |
| [011](rounds/011/round.md) | External clean ports | 201 queries; nine clean forced positions |
| [012](rounds/012/round.md) | Joint ports and minimization | 126 queries; 35-vertex inequality gadget |
| [013](rounds/013/round.md) | Actual two-copy chains | 64 queries; eight of 16 placements preserve both path patterns cleanly |
| [014](rounds/014/round.md) | Geometric triangle | First placement has exact clean canonical witness; zero solver queries |
| [015](rounds/015/round.md) | Equality diamond | All 64 fully clean layouts UNSAT |
| [016](rounds/016/round.md) | Diagnose diamond failure | All 64 layouts UNSAT without cleanliness |
| [017](rounds/017/round.md) | Direct equality ports | 596 queries over 172 new positions and first joint pair; clean equality gadget |
| [018](rounds/018/round.md) | Periodic equality wire | One UNSAT query, 64 pair checks, two triple checks and projection proof |
| [019](rounds/019/round.md) | Four-way junction | Eight wire triples and 216 pair checks; fixed first orientation fails |
| [020](rounds/020/round.md) | Asymmetric branch repair | 216 pair checks and one full check; reversed-endpoint junction succeeds |
| [021](rounds/021/round.md) | Junction extension | Two expanded junctions and a distance-two bound |
| [022](rounds/022/round.md) | Inequality attachment | Ninth canonical placement succeeds |
| [023](rounds/023/round.md) | Rational normalization | 68 motifs and explicit perturbation margin |
| [024](rounds/024/round.md) | Commensurate wire lengths | 256 transitions and normalized junction pass |
| [025](rounds/025/round.md) | Commensurate inequality | Four length combinations pass |
| [026](rounds/026/round.md) | Published source compiler | GJS Theorems 2.1--2.3 inspected |
| [027](rounds/027/round.md) | Published gadget transcription | 136 queries including a repaired transcription error |
| [028](rounds/028/round.md) | Proper-color source map | 112 initial cases; 114 after sparse repair, 452 queries total |
| [029](rounds/029/round.md) | Direct geometric crossing | 64 layouts fail both canonical patterns |
| [030](rounds/030/round.md) | Crossing diagnosis | 32 clean-extension queries UNSAT |
| [031](rounds/031/round.md) | Fixed orthogonal drawing | Graphviz certificate passes after quantization repair |
| [032](rounds/032/round.md) | Compressed crossover | 81 boundary queries and exact routing certificate |
| [033](rounds/033/round.md) | Junction-to-junction geometry | 36 full witnesses; sparse/dense checker agreement |
| [034](rounds/034/round.md) | Full geometric crossover | Two 409,345-vertex witnesses, 12,040 copies each |
| [035](rounds/035/round.md) | Independent solver encoding | Six CP-SAT primitive queries agree |
| [036](rounds/036/round.md) | Full planar source network | Six cases, four YES/two NO, 24 intermediate recoveries |
| [037](rounds/037/round.md) | General composition | Exact separation bounds and network-premise checks |
| [038](rounds/038/round.md) | Witness-independent geometry | Macro coordinates match; inconsistent network emits legally |
| [039](rounds/039/round.md) | Actual geometric target solving | YES/NO network decisions, six network recoveries |
| [040](rounds/040/round.md) | Both source maps and bounds | Empty-source subprocess checks; nonempty test-size blocker |
| [041](rounds/041/round.md) | Primitive scale intervals | 17 comparisons; equality admits 50q–53q |
| [042](rounds/042/round.md) | Wider-span chain | 256 clean induced motifs pass |
| [043](rounds/043/round.md) | Wider inequality interface | 16 connector witnesses pass |
| [044](rounds/044/round.md) | Nine-cell length adjustment | 72 full segment witnesses pass |
| [045](rounds/045/round.md) | Incident-range buses | Six decisions, 24 recoveries and geometric premises pass |
| [046](rounds/046/round.md) | Coordinate-rank compaction | Six networks preserve intersections; smaller projected sizes |
| [047](rounds/047/round.md) | Rational kink | 64 motifs: 56 clean, eight witness failures with repairs identified |
| [048](rounds/048/round.md) | Detoured unit wire | 72 complete one/two-unit witnesses pass |
| [049](rounds/049/round.md) | Detoured branching | 81 full stars pass |
| [050](rounds/050/round.md) | Finite interaction support | 72 exact support bounds pass |
| [051](rounds/051/round.md) | Compact complete map | 537,397-vertex actual YES witness; six recoveries |
| [052](rounds/052/round.md) | Certified local projection | 15,813 induced copies checked; projection SAT is unknown |
| [053](rounds/053/round.md) | Independent target witness search | Two phase queries; full YES coloring and six recoveries |
| [054](rounds/054/round.md) | Full-source NO certificate | 1,547,820 vertices certified NO; producer omission repaired |
| [055](rounds/055/round.md) | Oracle falsification | 516 graph and 5,422 witness comparisons; parser and numeric repairs |
| [056](rounds/056/round.md) | Broader full-source injection | Remaining four prepared cases pass; largest 4,059,987 vertices |
| [057](rounds/057/round.md) | All-length wire context | 108 wires and 324 exact boundary comparisons pass |
| [058](rounds/058/round.md) | Novelty reassessment | Published open case retained; WLAN full-text coverage gap |
| [059](rounds/059/round.md) | Finite forcing kernels | Two retained kernels independently infeasible; 204 queries |
| [060](rounds/060/round.md) | Noncanonical recovery | Eight alternate witnesses recover; eight fixed-exterior nonclean queries UNSAT |

## Work counts and verification closeout

Rounds 041--060 used **252 solver queries**: 236 Z3 and 16 CP-SAT. Integrated
verification added **25 queries**: 14 Z3 and 11 CP-SAT. Oracle self-tests are
excluded. There were 58 full-source recovery calls on independently found
or modified witnesses across the round scripts and integrated suites, plus
six candidate-provided witness recoveries and 24 intermediate-network
recoveries. Repeated and symmetry-equivalent calls are not distinct source
instances. Runtime/token totals for this allocation are unavailable.

The 20 rounds develop three construction mechanisms (wider-span straight
wires, network compaction, and rational detours) and one large-target
verification strategy. Proof, literature and adversarial-witness rounds
address obligations of the same reduction; they are not 20 independent ideas.

## Experience extraction

Shared files newly created: **0**. Existing shared files updated: **0**.
**Seven distinct destinations remain pending** because the user-supplied
campaign-only write scope excludes shared experience files. Every round
records its extraction decision and evidence. The pending destinations are:

1. `research/experience/hereditary-terminal-extension.md` — [001](rounds/001/round.md).
2. `research/experience/independent-replication-unit-disk-obstruction.md` — [003](rounds/003/round.md), [004](rounds/004/round.md).
3. `research/experience/unit-disk-false-twin-wire-obstruction.md` — [006](rounds/006/round.md).
4. `research/experience/rational-grid-three-subcoloring-obstruction.md` — [007](rounds/007/round.md)–[009](rounds/009/round.md).
5. `research/experience/subcoloring-terminal-composition.md` — [010](rounds/010/round.md)–[060](rounds/060/round.md), including exact scale intervals, rational detours and finite interaction contexts.
6. Existing `research/experience/compressed-variable-declarations.md` use update — [028](rounds/028/round.md), [040](rounds/040/round.md), [060](rounds/060/round.md).
7. `research/experience/induced-relation-projection.md` — [052](rounds/052/round.md)–[060](rounds/060/round.md): checked necessary projections for NO, restricted search with whole-graph validation for YES, and the omitted-inequality regression.

These are six proposed new entries and one existing-entry update, not seven
saved shared files. All 20 new round records contain extraction decisions;
links in the current proof and stage reports were checked at closeout.
