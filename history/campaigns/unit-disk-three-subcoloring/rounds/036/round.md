# Round 036 — source-to-planar-network crossbar

## Plan

Compile the verified proper-color source graph into one horizontal signal bus
per vertex and one vertical channel per edge. Use the fixed crossover for
nonincident bus/channel crossings. At the lower endpoint, turn the signal onto
the channel by equality; at the upper endpoint impose inequality with the bus.
Use 40-by-40 cells, extending the fixed macro's south/west ports by one unit.
Test all six prepared source formulas on the actual mixed network, solve it
independently with Z3, and recover sparse source assignments under six color
permutations for every YES instance. This is an intermediate target test, not
yet a full unit-disk source injection. Reuse the verified source/crossover
modules and compressed-variable experience; no new source restrictions.

## Evidence and diagnosis

All six intermediate targets match the source oracle: four SAT, two UNSAT;
24 color-permuted sparse recoveries pass. The largest tested network has
13,242 vertices, 17,088 segments and 225 crossover cells. Raw results in
[output.jsonl](output.jsonl), with actual networks and YES witnesses alongside.
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/036/probe.py`.
Counts: 12 solver queries, six intermediate injections, zero complete unit-disk
injections. No repairs; aggregate time/token usage unavailable.

Soundness follows by restricting every crossover to opposite-equal ports:
the horizontal bus recovers one color per original vertex, and the single
upper-endpoint inequality enforces each source graph edge. Completeness extends
a proper coloring independently through each published crossover. Sparse
source decoding then compares literal and true-palette bus colors.

Experience extraction: extend pending geometric-composition with the explicit
source crossbar and pending compressed-variable use history with successful
recovery. Shared writes remain restricted. Next establish the geometric
separation lemma for arbitrary such orthogonal networks.
