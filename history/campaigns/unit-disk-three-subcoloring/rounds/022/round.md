# Round 022 — inequality-to-wire connector

## Plan

Hypothesis: the inequality primitive can connect two independently extendable
equality wires. Put its ports at (0,0),(2,0). Place two equality copies outward
from each port along the horizontal axis, with step 3969/1000, a slight rational
compression of |D|. Verify every local copy's actual adjacency; do not rely
on approximate rotation. Consider all four inequality reflections/reversals
and all eight states independently on the left and right wire: 256 canonical
placements. Require the six skeleton terminals to have colors (0,0,0,1,1,1)
and to be clean. Stop at first success and save geometry, witness, and states.
No solver queries are planned; failure would only exclude this canonical family.

Use the period-one wires and round 021's distance-two interaction principle.
A successful connector still needs a scalable routing layout and polynomial
source construction, including arbitrary-distance length adjustment.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/022/probe.py`.
[Output](output.jsonl): the ninth canonical placement succeeds, with inequality
state (false,false), left wire state 1 and right wire state 0. The saved
[171-vertex connector](connector.json), [witness](witness.json), and
[states](states.json) include two equality copies per side and six clean ports.
Every inequality/equality copy has the intended induced adjacency. Zero solver
queries, source/recovery calls, or reruns.

The connector realizes inequality between the two outer wire ports by local
restriction, and its canonical witness handles any ordered distinct colors by
permutation. Only the stated finite extent has been checked. The wire step
3969/1000 differs slightly from |D| in the previous junction, so compatibility
requires normalization before assuming these primitives share a routing grid.

Experience extraction: update the pending composition finding with the actual
connector and the need to align geometric scales, not merely port color relations.
Its canonical left/right color states differ, which is already permitted by
the successful two-wire pair checks. Shared entry remains pending.

## Next action

Normalize all equality wires and the junction into the connector's rational
horizontal/vertical frame. Recheck the finite interaction motifs and obtain
strict distance margins for later small length adjustments. This addresses
scale compatibility and avoids building an ad hoc path-length controller.
