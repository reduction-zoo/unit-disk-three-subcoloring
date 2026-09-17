# Round 005 — irregular rational geometric obstructions

## Plan

Hypothesis: irregular point geometry exposes a three-color obstruction absent
from the tested grids. Such an obstruction could supply a critical palette
interface after deletion, but composition would still require proof. Sample
96 point sets: n in {24,36,48,60}, square side in {2,3,4}, seed in {0,...,7}.
For each combination use random.Random(10000*n+100*side+seed), distinct integer
coordinate pairs in [0,100*side]^2, divided by 100. Randomness is only discovery;
no resulting reduction may use it. One exact Z3 three-color query per set.
Stop on the first UNSAT set and preserve its coordinates; otherwise finish all
96. No timeout or background process. A result concerns only sampled instances.

Relation to evidence: irregular hosts change the geometric family after grids
failed to constrain colors. Round 001's restriction lemma permits reusing SAT
witnesses to exclude subsets. Shared search found no applicable palette entry;
complete-join replication remains excluded by rounds 003--004.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/005/probe.py`.
[Raw output](output.jsonl): all 96 declared samples are SAT, with independently
validated witnesses. Ninety-six geometric instances and solver queries; zero
source injections and zero recovery calls. No repair or rerun; usage unavailable.
This is evidence about these samples only. It neither proves a universal
three-color upper bound nor excludes logical gadgets with terminals.

Supporting searches on 2026-09-16 used `"subcoloring" "unit disk" "three colors"`,
`"subchromatic" "unit disk" "lower"`, `"cluster coloring" "unit disk" complexity`,
and `"subcolouring" "unit disc"`. No matching explicit four-color obstruction
was found. Search absence is not a theorem. In inspecting the published
co-comparability palette route, K2,3 emerged as a smaller geometric obstruction;
this suggests auditing the wire independently of its already excluded palette.

Experience extraction: none new. Sample satisfiability has no established
structural cause beyond the saved witnesses. Do not turn this observation into
an assertion that irregular geometric gadgets are impossible.

## Next action

Investigate the published false-twin wire, not larger random samples. A five-vertex
forbidden subgraph could show that replacing only its palette is insufficient.
This would change the next construction choice before more coordinate search.
Short-term prospects remain low (uncalibrated); no geometric NO or forcing gadget.
