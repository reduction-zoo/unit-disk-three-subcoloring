# Round 009 — pair interfaces exposed by vertex deletion

## Plan

Hypothesis: removing a minimum-degree vertex from the 34-vertex critical seed
forces an equality or inequality between former neighbors. Test each of the
four degree-eight vertices (indices 3,9,29,33 in critical.json), each of the 28
pairs in its neighborhood, and both possible pair relations. Scope: 224 exact
three-color queries. Record every UNSAT relation and every SAT witness. These
are four interface templates from one seed, not four independent routes.

The full reduction would interpret a forced relation as a signal or palette
connection. Terminal accessibility and composition are unresolved. Use the
pending restriction and critical-grid findings from rounds 001/008 locally;
no additional applicable shared experience was found. Finish the fixed scope,
then select a relation for minimization if one exists.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/009/probe.py`.
[Output](output.jsonl): 224 queries, 148 SAT and 76 UNSAT. Every tested pair
has at least one feasible relation. Deletions 3 and 9 each fix all 28 pair
relations among former neighbors; deletions 29 and 33 each fix ten. All SAT
witnesses pass the component checker. Four templates; no source or recovery
calls. No rerun; usage unavailable.

This supplies real geometric equality and inequality interfaces. For example,
removing vertex 3 forces vertices 0 and 17 equal, and vertices 0 and 4 different.
These are computational claims about the saved finite graph, not a general
reduction or an independent review. The cause is loss of extension at the
critical seed's boundary; the mechanism of each forced relation still needs
a short combinatorial proof or verifiable finite certificate.

Experience extraction: update the pending grid-obstruction entry with these
interface queries and exact indices. It remains one finding file proposal.
Do not yet recommend arbitrary identification of its terminals: monochromatic
neighbors in separate gadgets can form a new P3 at an identified vertex.

## Next action

Test terminal cleanliness before shrinking the gadgets. For each of the 76
forced relations, require both terminals to have no same-colored internal
neighbor. Existence of such witnesses would provide a sufficient completeness
condition for gluing copies at a single terminal, subject to geometric separation.
If none exist, construct exposed ports or abandon this mode of composition.
