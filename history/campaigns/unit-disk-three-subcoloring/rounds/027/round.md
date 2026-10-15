# Round 027 — exact published source gadgets

## Plan

Transcribe GJS Figures 1 and 2 using explicit edge lists. Check all 27 clause
input color assignments and all 81 crossover port assignments with Z3, against
the printed properties. This is a known baseline, not discovery. Save a
canonical completion for each valid boundary pattern. The first check will
reject a transcription error or reveal a missing premise before geometric
compilation. No shared experience applies beyond the local composition records.

## Evidence and diagnosis

The first run reached the crossover and rejected its all-equal boundary.
[transcription-failure.jsonl](transcription-failure.jsonl) preserves 28 queries.
The diagram has only alternating outer-square edges; four extra edges had been
transcribed. Removing those four edges repairs the transcription. The rerun
passes all 27 clause patterns and all 81 crossover patterns, with canonical
completions in [output.jsonl](output.jsonl). Total 136 solver queries, including
the failed run. No source injection or recovery call yet. Time/token unavailable.

The 24-edge crossover allows exactly the nine opposite-equal port patterns.
The clause output fixed to color 0 extends precisely except when all inputs
are color 1 or all color 2. Boolean inputs in {0,1} therefore implement OR.
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/027/probe.py`.
Experience extraction: none new; this confirms a published baseline after an
ordinary transcription repair. Next assemble actual formulas, including NO cases.
