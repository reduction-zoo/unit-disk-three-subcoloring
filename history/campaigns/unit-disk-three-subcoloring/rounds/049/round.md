# Round 049 — branching with detoured arms

## Plan

The new detour has lateral extent absent from the previous proof. Test a
four-arm star with two grid units per arm and a fixed center color 0, across
all 3^4=81 assignments to the four outer hubs. Equal endpoint colors select
equality; others select inequality. This covers all relation patterns and
both noncentral color choices, up to global permutation. Check full sparse
colorings and induced primitives. Derive exact strip bounds and identify
whether a monochromatic P3 can touch two arms beyond their first hub cells.
Completion: all 81 checks and an explicit bound, or first counterexample.
Experience: use round 048's complete segments, but do not assume their
isolated validity guarantees branching completeness.

## Evidence and diagnosis

All 81 four-arm star colorings pass with induced primitives in
[output.jsonl](output.jsonl); command `python3 rounds/049/probe.py` from the
campaign directory. Zero solver queries, repairs or reruns. This covers every
first-two-unit branching color pattern up to global permutation. A proposed
finite-neighborhood proof classifies P3 interactions into one/two adjacent
units, a star neighborhood, and disjoint grid features. Exact Euclidean strip
bounds still need a separate certificate; they are not inferred from passing
stars. Experience extraction: pending geometric-composition update; shared
writes remain out of scope. Next: establish a geometry-only finite interaction
certificate independently of witness colors.
