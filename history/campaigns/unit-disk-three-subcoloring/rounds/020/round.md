# Round 020 — asymmetric branch ports and alternative witnesses

## Plan

Hypothesis: the four-way junction can be repaired by using the other endpoint
of the asymmetric equality gadget at its center, or by selecting another
internal coloring. Repeat round 019's compatibility experiment with first-arm
state 4 (reversed, unreflected, no color swap); the other three arms range over
eight states. Scope: 216 pair checks and at most 512 full canonical checks.
Stop on first clean canonical success.

If no canonical success exists, rank the 512 state combinations by the number
of passing pair checks (descending, lexicographic tie-break). Take the first
eight distinct geometric layouts, ignoring color-swap bits for deduplication.
For each, query Z3 for a clean coloring with all five skeleton ports color 0.
Stop on first SAT result; at most eight solver queries. Record whether a solver
witness differs from the fixed canonical lifting. No timeout. This consumes
the last authorized round; complete-rule proof obligations remain regardless
of whether a local junction succeeds.

Use round 019's diagnosis and the pending periodic-wire/composition evidence.
No applicable shared finding settles this asymmetric-port question.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/020/probe.py`.
[Output](output.jsonl): 216 pair checks; the first surviving full combination,
states (4,4,4,4), has a clean canonical coloring. One full four-arm check, zero
solver queries. The conditional alternative-witness search was not executed.
The [137-vertex junction](junction.json), [witness](witness.json), and
[states](states.json) are saved. No repair/rerun, source/recovery calls, or
measured usage.

The asymmetric-port diagnosis was productive: putting the reversed endpoint
at the center repairs the canonical composition. This does not contradict
round 019, which fixed the other endpoint. Restriction to the four induced
equality copies forces all five ports equal; the canonical witness and color
permutation give clean completeness. Extension by arbitrary additional wire
copies has not been checked at the junction, and is not implied by the separate
straight-wire lemma alone.

Experience extraction: update the pending terminal-composition finding with
the contrasting first-endpoint failure and second-endpoint success. An equal
logical relation does not make its geometric ports interchangeable. Both the
failed and successful placements are retained. Five distinct shared-entry
proposals remain pending under the user-supplied campaign write scope; no
shared entry is claimed as saved.

## Next action and allocation close

The 20-round allocation is exhausted. Stop discovery with partial progress,
not a complete Karp rule. The next discriminating task, if another allocation
is provided, is to attach continuing wires to the junction and to the inequality
primitive using actual coordinates, then prove a scalable routing construction.
A fixed NP-hard source embedding, deterministic forward map, universal recovery,
polynomial size/bit bounds, and independent full-rule review remain absent.
Short-term prospects are **unknown**, uncalibrated: local interfaces and straight
propagation are now supported, but a general routing/composition lemma is missing.
No new round is started by closeout verification of the existing artifacts.
