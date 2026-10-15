# Round 050 — finite interaction support certificate

## Plan

Replace the old straight-cell separation argument by an explicit unit-block
support argument. Generate both relation types in four directions with two
units and all endpoint color pairs. Verify every emitted point lies within
90q of its underlying segment (using exact squared distances); 90q is a
conservative rational bound. Then 334q-180q>2 separates graph features at
one integer-grid unit of distance. Check the strict inequality exactly.
Together with the 81 stars and one/two-unit checks this leaves only the
classification of intersecting grid features, already constrained to shared
endpoints by the network compiler. This is a general-proof strategy, not a
new numerical parameter sweep. Completion: 72 exact support checks and
written scope of the resulting conditional lemma. Reuse rounds 046/048/049.

## Evidence and diagnosis

All 72 exact support checks pass in [output.jsonl](output.jsonl), generated
by `python3 rounds/050/probe.py` from the campaign directory. The rational
separation gap is 154q>2. These checks cover all unit templates and endpoint
hubs; longer wires repeat the same equality unit. P3s meeting nonincident
integer-grid features are excluded by distance. Incident features require
the finite star and consecutive-unit certificates, not this distance bound
alone. Zero solver queries, repairs or reruns. Experience extraction:
pending geometric-composition entry, with an unreviewed finite-neighborhood
proof and explicit scope; shared writes remain blocked.
Next: integrate the smaller compiler and exercise an actual nonempty target.
