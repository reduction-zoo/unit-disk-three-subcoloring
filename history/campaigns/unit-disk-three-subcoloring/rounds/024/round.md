# Round 024 — commensurate wire lengths

## Plan

Hypothesis: equality copies with lengths 52q and 53q, q=749/10000, preserve
both their local relation and all canonical pair transitions. These lengths
are 3.8948 and 3.9697; their coprime integer coefficients permit exact routing
lengths without accumulated numerical approximation. Test all 64 state pairs
for each of four ordered length pairs: 256 geometric checks. Verify induced
local adjacency and cleanliness in every case. Also check the reversed-port
junction scaled to length 52q. No solver query or timeout.

If successful, an inequality span 27q would fit a grid of spacing 2756q, since
2756-2*52-27=25*52+25*53. Its actual connector must be checked next; arithmetic
alone cannot justify geometric compatibility. Use round 023's normalization
result and the current exact local gadget files. This changes routing lengths,
not the fixed NP-hardness target.

## Evidence and diagnosis

All 256 ordered length/state transitions passed exact induced-adjacency and
clean-witness checks. The normalized 137-vertex junction also passed.
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/024/probe.py`;
raw evidence: [output.jsonl](output.jsonl). Zero solver queries, source
injections or recovery calls; no repairs. Time/token usage unavailable.

Experience extraction: extend the pending geometric-composition entry with
commensurate lengths and all-state transitions. Its shared destination remains
blocked by campaign-only writes. This supports exact integer routing arithmetic,
not a complete graph embedding. Next test the expanded inequality connector.
