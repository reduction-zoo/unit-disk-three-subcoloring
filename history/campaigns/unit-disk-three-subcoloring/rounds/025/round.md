# Round 025 — commensurate inequality connector

## Plan

Reuse the successful round 022 attachment: left state 1, right state 0.
Scale the inequality span from 2 to 27q and independently choose each wire
length from 52q and 53q. Test four length combinations, both induced local
adjacency and the complete clean canonical witness. If these pass, calculate
projection separation for further extensions. No solver query. This addresses
the remaining interface before planar graph compilation. Prior composition
experience is recorded in rounds 021--024; shared search returned no applicable
existing planar geometric routing lemma.

## Evidence and diagnosis

All four length choices pass induced-adjacency and full clean-witness checks
in [output.jsonl](output.jsonl), using the command `python3
campaigns/unit-disk-three-subcoloring/rounds/025/probe.py`. No solver queries,
source injections, recovery calls or repairs. Time/token usage unavailable.
The expanded inequality fits the same rational quantum as both wire lengths.
The remote-extension bound and source compiler remain obligations.

Experience extraction: extend pending subcoloring-terminal-composition.md
with this measured connector compatibility; campaign-only write restriction
prevents the shared update. Next inspect the original planar three-coloring
construction instead of inventing a crossover.
