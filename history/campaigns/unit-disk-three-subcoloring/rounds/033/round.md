# Round 033 — geometric routed edges between junctions

## Plan

Use grid spacing 1535q: an equal segment between 52q junction arms takes
27 long cells; an unequal segment takes 27 short cells plus one 27q inequality.
Each extra grid unit adds two short and 27 long cells. Check unit segments
in four orientations and every ordered endpoint color pair allowed by the
relation (36 complete witnesses). Place the inequality after 13 short cells
and choose its adjacent equality witnesses from round 025. Use exact integer
spatial buckets for the expanded geometric checker; cross-check this checker
against the existing rational dense checker on the five saved small primitives.
This is the smallest direct way to test expanded graphs without quadratic
storage. No solver query is planned. Experience: reuse all-state transitions
and remote separation bounds, with actual geometry as the discriminating check.

## Evidence and diagnosis

All 36 fully expanded routed-edge witnesses pass exact geometric P3 checks,
and every primitive's induced adjacency matches its saved base graph. The
sparse integer checker agrees with the dense rational checker on all five
saved primitives. Zero solver queries, no source injections/recovery calls,
no repairs; time/token unavailable. Command: `python3
campaigns/unit-disk-three-subcoloring/rounds/033/probe.py`; raw [output.jsonl](output.jsonl).

Grid spacing 1535q uses 29k-2 equality cells on a k-unit segment, with one
inequality cell when requested. It reduces the previous candidate spacing
using exact length identities, without a new geometric assumption.
Experience extraction: extend pending geometric-composition with tested
junction-to-junction routes. Shared destination restricted. Next expand the
complete fixed crossover, where nearby parallel routes and bends coexist.
