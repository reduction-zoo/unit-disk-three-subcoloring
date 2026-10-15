# Round 002 — geometric obstruction baseline

## Plan

Round 001 excludes pair forcing on the initial grid. Hypothesis: changing the
spacing and extent supplies a graph requiring four subcolors, a source for
critical local constraints. Test the 12 full square grids with side lengths
4, 5, 6 and spacings 1/2, 2/5, 1/3, 3/5. One three-color query each; preserve
all witnesses and any UNSAT grid. No timeout. A NO graph is only a starting
point: terminal semantics and composable embeddings would remain unresolved.

Experience retrieval: use round 001's host-extension result locally. Shared
search already found no unit-disk palette entry; do not repeat the same host.
The objective here differs from pair enumeration: find a geometric NO baseline.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/002/probe.py`.
[Raw output](output.jsonl): all 12 grids are SAT, with independently checked
witnesses on 16, 25, or 36 vertices. Twelve templates and solver queries; zero
source/recovery calls. No rerun. Time/token usage unavailable.

This excludes these full grids and their induced subgraphs as unconditioned
NO gadgets. It does not exclude terminal constraints on them or non-grid graphs.
The missing geometric NO baseline remains a preparation limitation. Search
queries `"unit disk graphs" "subchromatic number" "four"`,
`"unit disk" "subcoloring" "hexagonal"`, and `"subchromatic" "plane" coloring`
on 2026-09-16 did not locate a usable explicit four-color lower-bound example.
The primary full version, Observation 4, proves an upper bound of seven; it
is not evidence that seven or four are necessary.

Experience extraction: none new. The induced-subgraph restriction consequence
is already covered by round 001's pending entry; these 12 witnesses add only a
finite tested family, not a new construction principle.

## Next action

Change mechanism: investigate reduction from proper three-coloring by independent
vertex replication. It supplies a direct semantic route independent of a palette,
but its unit-disk geometry must be checked before implementation. Prospects for
the grid route are low (uncalibrated), not a conclusion about the open problem.
