# Round 038 — construct geometry without a satisfying coloring

## Plan

Implement the geometric network map with no solver import, witness argument,
or satisfiability decision. Compare its complete emitted coordinate sequence
with the saved 409,345-vertex macro. Also construct a four-edge rectangular
network with three equalities and one inequality, which has no coloring; it
must still emit valid rational centers. This closes the witness-dependent
experimental-constructor gap. The small inconsistent rectangle is retained for
an independent actual-target NO test next. No solver queries in this round.
Reuse exact local coordinate templates and the sparse-variable lesson's
requirement that construction never allocate by numeric label magnitude.

## Evidence and diagnosis

The pure coordinate emitter reproduces all 409,345 saved macro coordinates
in their original order, without receiving any coloring or importing a solver.
It also emits a valid 4,250-vertex target for the inconsistent rectangle.
Raw results: [output.jsonl](output.jsonl). Command: `python3
campaigns/unit-disk-three-subcoloring/rounds/038/probe.py`. No solver queries,
no source injections or repairs; time/token unavailable.

The callback only receives coordinates for writing/counting; it does not choose
construction steps. The emitter returns deterministic hub indices for recovery.
Experience extraction: extend pending geometric-composition with the witness-
independent emitter check. Shared destination restricted. Next independently
solve actual geometric YES and NO rectangle outputs.
