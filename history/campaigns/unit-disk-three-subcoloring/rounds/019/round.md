# Round 019 — four-way equality junction

## Plan

Hypothesis: four equality copies can meet at a clean common terminal, providing
branching and right-angle routing. Use directions D, rot90(D), -D, -rot90(D).
Fix the first arm to round 018's state 0. For the other three arms, consider
each of eight reflection/reversal/color-swap states: 512 combinations. First
check eight constant-state straight-wire triples. Restrict arms to states whose
triple witness passes. Check pairwise arm compatibility to avoid unnecessary
full checks, then test the full four-arm coloring on surviving combinations,
stopping at first success. At most 216 pair checks and 512 full checks; no SAT
query is required for a passing canonical witness. Failed canonical checks do
not prove graph infeasibility. Save the first successful junction and witness.

Use round 018's periodic wire and projection argument. Extendability beyond the
first arm copies is an explicit remaining obligation, to be analyzed from
coordinate bounds and the final round rather than silently assumed.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/019/probe.py`.
[Output](output.jsonl): all eight constant-state wire triples pass. Of 216 arm
pair checks, every opposite-arm pair passes, but some adjacent-arm pairs fail.
In particular, fixed arm 0/state 0 is incompatible with all eight states on
arm 3. No four-arm combination survives pair filtering, so zero full four-arm
checks and zero solver queries were performed. This excludes the declared
canonical-witness family with first state 0, not the graphs' colorability.
No repair/rerun, source/recovery calls, or measured usage.

The fixed first-arm orientation is now implicated. Endpoint reversal changes
which asymmetric port of the seed sits at the branch, so it cannot be dismissed
as an equivalent geometric choice. Separately, a different internal coloring
could repair a canonical witness failure. Both questions should be checked
before declaring this junction geometry impossible.

Experience extraction: none new. The failure remains witness-family-specific;
record it in the pending composition entry without claiming UNSAT. Eight
straight-wire states are retained as positive evidence.

## Next action

Use the final allocated round to reverse the first arm, then query alternative
internal colorings on a bounded set of promising layouts if canonical lifting
still fails. This separates asymmetric-port failure from an overrestricted
witness choice. Do not spend another round without a new user allocation.
