# Round 057 — arbitrary-length wire neighborhoods

## Plan

The one/two-unit certificates must cover interior units of arbitrarily long
wires, not only units touching endpoint hubs. Test lengths three, four and
five units in four directions and all nine endpoint color pairs: 108 wires.
For every internal unit boundary, normalize coordinates and signal color,
and compare the width-four strip centered there with the boundary strip of
the two-unit equality template. A P3 crossing a boundary has all its points
within distance two longitudinally, so this exact strip comparison addresses
the missing local context. Check complete colorings and induced primitives.
The support gap from round 050 excludes nonconsecutive units; record the
all-length inference separately from the finite tests. Reuse pending geometric
composition evidence. Completion: 108 checks and all boundary comparisons,
or a saved counterexample to the neighborhood classification.

## Evidence and diagnosis

All 108 full wire checks and 324 internal-boundary comparisons pass in
[output.jsonl](output.jsonl); command `python3 rounds/057/probe.py` from the
campaign directory. Zero solver queries, repairs or reruns. Each internal
boundary's normalized width-four strip is the same fixed two-cell context.
This identity also follows from the emitter: the boundary is always formed
by two collinear length-52q equality cells in state 4. The nearest detour
ends more than two away, so changing the number or type of earlier units
cannot alter that strip. Unit interiors repeat the checked equality template;
only the first unit may contain I. A P3 either stays within one unit, crosses
one boundary, or would meet two nonconsecutive units, excluded by the support
gap. This closes the stated middle-unit obligation in the author argument.
The argument and finite certificate interpretation remain independently unreviewed.
Experience extraction: pending geometric-composition entry gains the exact
boundary-context criterion; shared writes remain blocked.
Next: reassess novelty against later versions and equivalent formulations.
