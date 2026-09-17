# Round 018 — periodic straight equality wire

## Plan

Hypothesis: the direct equality gadget supports a periodic chain of arbitrary
length with clean junctions. First query unequal terminal colors without
anchor pins. Then consider eight copy states: endpoint reversal, reflection
across its terminal line, and swapping its two nonterminal colors. Normalize
positions relative to the first port, with displacement D=(-13/5,3). For all
64 ordered state pairs, check the canonical coloring of two adjacent copies.
For period-one/two patterns passing these checks, test three consecutive copies
in every phase, stopping at the first successful periodic pattern.

Check every local induced copy and terminal cleanliness. Bound projection onto
D to exclude edges between nonconsecutive copies; with that bound, every P3
is contained in at most three consecutive copies. A successful periodic check
then proves clean completeness for every chain length, conditional on the base
finite gadget. At most one solver query, 64 pair checks and 128 triple checks.
No timeout. Save the exact pattern and witnesses. Use the pending restriction
and composition findings; this supplies a scalable primitive, not a full source
encoding or branching theorem.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/018/probe.py`.
[Output](output.jsonl): unpinned unequal terminals are UNSAT (one solver query).
All eight copy states have projection interval contained in [0,1] along D,
with squared step length 394/25. The 64 pair checks are recorded; state pair
(0,0) passes, as do both checked triple phases. The selected pattern is the
constant unreflected, unreversed state with no internal color swap.
[Pattern](pattern.json), [three-copy graph](three-copy.json), [witness](witness.json).
No rerun, source/recovery calls, or measured usage.

General straight-wire argument: copies whose indices differ by at least two
are separated in projection by at least |D| > 1, so no edge joins them. Every
P3 is therefore contained in at most three consecutive copies. The saved
period-one triple witness, translated and repeated, excludes every such P3
and keeps every junction clean. Restriction to the induced equality copies
forces all chain terminals equal. This proves the all-length implication
conditional on the finite base-gadget check, not by extrapolating test counts.
The construction and canonical coloring take polynomial time and linear output
size in the number of copies; coordinates translate by rational multiples of D.

Experience extraction: update the pending terminal-composition finding with
the projection bound and periodic local-to-global argument. The finding now
includes a supported scalable wire, unlike the earlier arbitrary-gluing claim.
No independent review or complete 3-SAT rule is implied.

## Next action

Test a four-way equality junction with four rotated copies at one common
terminal, keeping outer terminals clean. If it succeeds, investigate how to
extend its arms and how geometric routing connects the inequality primitive.
Only two allocated rounds remain; these obligations must not be hidden by the
successful straight-wire lemma.
