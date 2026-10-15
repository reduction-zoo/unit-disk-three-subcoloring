# Round 031 — fixed orthogonal crossover layout

## Plan

Use the published planar 13-vertex crossover. Replace vertices of degree above
four by small equality cycles in their geometric cyclic order, preserving
proper inequality incidences. All resulting vertices have degree at most four.
Ask installed Graphviz `neato -n2` for one orthogonal layout using explicit
planar initial positions, then inspect its polylines for unrelated intersections.
This finite single-layout experiment avoids implementing a general drawing
framework. A passing layout can become a fixed coordinate certificate; a failed
layout is only a failure of this drawing, not the graph's orthogonal embeddability.
No applicable shared routing result was found.

## Evidence and diagnosis

Graphviz produced one layout of the split crossover. Rounding to single units
left four tiny diagonal attachments and two overlaps; [fine-grid-failure.json](fine-grid-failure.json)
preserves that failure. Quantizing the same drawing to ten units removes those
attachment artifacts. The actual final 44 paths and 152 segments have zero
nonorthogonal segments or unrelated intersections in [layout-check.json](layout-check.json).
No layout search or new graph was introduced in this transcription repair.
Commands: `python3 .../rounds/031/probe.py` and `python3 .../rounds/031/check_layout.py`
from the repository root, with `...` denoting the campaign path.
No solver queries, source injections or recovery calls. Time/token unavailable.

This is a fixed routing certificate, not a guarantee about Graphviz on arbitrary
inputs. The split graph and its semantic relation need explicit checking next.
Experience extraction: propose fixed-certificate routing as an extension of the
pending geometric-composition entry; exact rational intersection checking is its
necessary premise. Shared destination remains restricted.
