# Round 037 — general orthogonal-network composition

## Plan

Prove that the finite geometric interfaces extend to every noncrossing
axis-aligned integer-grid network of maximum degree four after scaling by
1535q. Calculate exact projection bounds for both E lengths, all eight states,
and the I core. Divide possible monochromatic P3s into local motifs, incident
arm interactions, and unrelated grid features. Check the crossbar's geometric
premises on all six saved networks. No solver query. This converts successful
finite macros into a general argument; failure leaves a concrete missing
interaction class rather than a claimed theorem. Reuse rounds 024--025 and
033 plus the pending clean-composition evidence.

## Evidence and diagnosis

All exact distance-two bounds pass, and all six saved crossbar networks have
maximum degree four and no unintended intersections. The general argument is
in [composition.md](composition.md), with numeric constants and network checks
in [output.jsonl](output.jsonl). Command: `python3
campaigns/unit-disk-three-subcoloring/rounds/037/probe.py`. Zero solver queries,
no source injections or repairs; time/token unavailable.

A remaining implementation gap is explicit: the experiment constructor accepts
a network coloring to generate its witness, although its coordinates do not
mathematically depend on that coloring. The forward map must emit those
coordinates on NO networks without solving anything. Next isolate that map and
check byte-for-byte coordinate equality against the two saved macro witnesses.
Experience extraction: extend pending geometric-composition with the precise
distance-two interaction partition and its network premises. Shared write
restriction remains in force.
