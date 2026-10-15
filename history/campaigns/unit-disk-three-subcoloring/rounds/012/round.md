# Round 012 — joint inequality gadget and minimization

## Plan

Hypothesis: one left color-2 port and one right color-1 port from round 011
coexist as clean, forced-different terminals. Test all 20 combinations, each
with equality, inequality, and clean inequality (60 queries). Prefer the pair
(2/5,-2/5),(12/5,-2/5) if successful, because equal height and maximal tested
horizontal separation simplify composition. Otherwise use the first successful
pair in the logged order. This is an explicit research choice, not a runtime
fallback in a candidate algorithm.

For the selected graph, try deleting each of the 33 core vertices once; keep a
deletion only if a clean-different witness exists and equality is UNSAT. At most
66 further queries. Keep both terminals. Save the final gadget and all witnesses.
Use round 010's sufficient composition condition and round 011's exposed ports.
No complete-rule claim; repeated-copy geometry and a source encoding remain.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/012/probe.py`.
[Output](output.jsonl): all 20 joint port combinations forbid equality and admit
both ordinary and clean inequality witnesses. Sixty joint queries plus 66
deletion queries. None of the 33 core vertices could be removed while preserving
the stated interface. The [35-vertex gadget](gadget.json) has terminals 33 and 34
at (2/5,-2/5),(12/5,-2/5). Its relation is precisely inequality: color permutation
extends the checked (0,1) witness to every ordered pair of distinct colors.
Equal colors are computationally excluded. This is a finite gadget result,
not yet a full reduction or independently reviewed proof. No rerun; usage
unavailable. No source or recovery calls.

Experience extraction: update the pending terminal-composition entry with joint
rather than individual port evidence, all 20 pairings, and the preserved gadget.
Do not count each pairing as a new insight. No new distinct pending file.

## Next action

Test two actual geometric copies sharing one terminal, including mirror and
endpoint orientation choices. Use actual distance-derived cross edges and
independent global coloring checks; an abstract edge relation is insufficient.
If a chain realizes the expected two-edge path relation, try a triangle and
then an equality diamond. Short-term prospects remain unknown: composition now
has a testable primitive, but no scalable wire or source encoding exists.
