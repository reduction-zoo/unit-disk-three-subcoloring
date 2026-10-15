# Round 010 — safe terminal composition

## Plan

Hypothesis: the forced pairs from round 009 admit colorings in which both
terminals have no neighbor of their own color. Such witnesses compose safely
when gadgets share only terminals and have no unintended cross edges.
For each of the 76 forced relations, solve with the opposite of its recorded
UNSAT relation and with all internal neighbors different at both terminals.
Scope: exactly 76 queries on the four 33-vertex hosts. Preserve witnesses.
Geometry of placing copies remains unresolved even on success. This checks
composition before local minimization, as required by research-propose.

Experience: use the critical seed and pair results from rounds 008--009 locally.
The common P3-at-a-junction failure is diagnosed directly here, not inferred
from unrelated matching-cut entries. No applicable shared entry is available.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/010/probe.py`.
[Output](output.jsonl): all 76 clean-pair queries are UNSAT. Thus none of these
forced pairs supports the proposed sufficient gluing condition on its unchanged
33-vertex host. This does not prove that all compositions fail: one could align
monochromatic cliques or use new exposed ports. No solver ambiguity, rerun, or
repair; usage unavailable. No source or recovery calls.

The failure is localized to completeness at the terminal. Pair semantics alone
are insufficient: after identifying copies at a terminal, same-colored internal
neighbors from different copies form a forbidden P3 if no cross edge joins them.
The cleanliness condition avoids that problem but is unavailable for all tested
interfaces. Soundness of the individual pair relations remains intact.

Experience extraction: pending proposed entry
`research/experience/subcoloring-terminal-composition.md`. Claim: pair constraints
alone do not certify gluing; absence of monochromatic terminal neighbors is a
sufficient completeness condition for edge-disjoint gadget interiors with no
cross edges. Counterevidence: these 76 pairs fail that sufficient condition.
Scope and review: main-agent lemma plus finite UNSAT checks, not a universal
composition impossibility. Shared writes remain out of the user-supplied scope.

## Next action

Try new vertices outside the seed's lower boundary as exposed ports. Query their
colors relative to the forced three-color palette and test cleanliness when a
color is uniquely forced. This changes the interface rather than weakening its
composition requirement. Prospects remain unknown (uncalibrated).
