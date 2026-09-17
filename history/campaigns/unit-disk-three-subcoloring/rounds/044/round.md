# Round 044 — nine-cell commensurate segment

## Plan

Replace spacing 1535q by 581q. Between 52q junction arms, an equality edge
uses nine 53q cells; an inequality edge uses nine 50q cells plus one 27q
inequality gadget after cell four. Each additional grid unit contributes
two 52q cells and nine 53q cells. The span equations hold exactly.
Test one- and two-unit segments in four directions and all nine endpoint
color pairs: 72 complete witnesses. Check every primitive remains induced
and every resulting monochromatic component is a clique. The new mechanism
is common short spacing, supported by rounds 041--043. This does not test
full-source outputs. Completion: all 72 cases or a saved first counterexample.
Experience: pending composition finding supplies the interaction checks;
the new possible failure is proximity of the connector to an endpoint hub.

## Evidence and diagnosis

[output.jsonl](output.jsonl) contains all 72 passing complete-segment checks.
Run `python3 rounds/044/probe.py` from the campaign directory. Every primitive
retains its induced graph; each full witness passes the sparse P3 validator.
There were zero solver queries, repairs or reruns. The new spacing is 581q;
vertex count becomes 137v+374ell-69e+34h for the same network. This is still
finite evidence. Full-source targets remain millions of vertices.
Experience extraction: pending geometric-composition update, with the new
spacing, exact count and finite scope; shared writes are outside scope.
Next: eliminate bus tails that serve no source edge, addressing network size
rather than repeating scale variations.
