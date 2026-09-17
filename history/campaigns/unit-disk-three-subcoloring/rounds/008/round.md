# Round 008 — independent obstruction check and minimization

## Plan

Hypothesis: round 007's grid has a small vertex-critical obstruction useful for
an extension interface. Independently encode geometry using integer arithmetic
on the saved common denominator, Boolean color indicators with exactly one
color per vertex, and direct ordered-center P3 enumeration. First confirm the
49-vertex NO and obtain a four-color witness, then greedily try deleting each
original vertex once. Keep a deletion only when the Boolean solver returns
UNSAT. Save SAT witnesses for failed deletions. Scope: at most 51 solver queries
(2 baseline + 49 deletions), no timeout. One pass suffices for vertex minimality:
a coloring of an earlier deletion restricts to all subsequent induced subsets.

Use round 001's local restriction lemma and round 007's pending obstruction.
No shared entry supplies this geometric baseline. Novelty of a small obstruction
is not presumed; the objective is a reduction interface, not an extremal paper.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/008/probe.py`.
[Output](output.jsonl): independent Boolean encoding confirms the 49-vertex
three-color UNSAT result and supplies a valid four-color witness. Forty-nine
deletion queries remove 15 vertices, leaving a [34-vertex obstruction](critical.json)
with [original indices](indices.json). Exactly 51 queries, zero source/recovery
calls. Both encodings use Z3, so solver implementation is not independent;
geometry and constraint code are separate. No repairs/reruns; usage unavailable.

For every retained vertex v, the failed deletion produced a coloring on an
earlier superset minus v. Restrict that witness to the final graph minus v.
It remains valid, proving vertex minimality conditional on the verified UNSAT
claim. The four-color witness also restricts, so the final graph has exactly
four subcolors under the same computational evidence. No human proof of this
particular UNSAT result or independent review has been obtained.

Experience extraction: update the pending grid-obstruction entry from round 007
with the independent encoding, four-color witness, and critical subgraph.
The minimality argument reuses round 001's pending restriction lemma. No new
shared file or additional distinct pending entry. The original NO regression
is now backed by two encodings, allowing its addition to the prepared self-test.

## Next action

Delete each of the four degree-eight vertices and inspect all pairs among its
eight former neighbors for forced agreement/disagreement. This uses the critical
obstruction's extension failure to target a concrete boundary interface, rather
than sampling more arbitrary graphs. Even a forced relation still needs an
accessible terminal, propagation, clauses, and polynomial geometric composition.
Short-term prospects: unknown, uncalibrated; now there is a real critical seed.
