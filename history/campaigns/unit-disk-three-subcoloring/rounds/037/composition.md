# Conditional geometric compilation lemma

Let H be a finite graph whose vertices have distinct integer-grid positions.
Each edge is a nonzero horizontal or vertical segment, and two segments
intersect only at a shared endpoint. Assume maximum degree at most four.
Label each edge either equality or inequality of three colors. The geometric
construction below represents exactly the satisfying color assignments of H,
conditional on the two finite forcing lemmas for E and I.

## Construction and local evidence

Set q=749/10000 and S=1535q. Multiply grid positions by S and place the
four-arm junction at each vertex. Every arm has length 52q. A segment of k
grid units has the following interior cells between its two junction arms:

- Equality: 27 cells of length 53q, then k-1 repetitions of two cells of
  length 52q and 27 cells of length 53q.
- Inequality: 27 cells of length 52q, with I of span 27q after the first
  13 cells, then the same k-1 repetitions.

Both choices have the required total span Sk after including the arms.
Free cells use the fixed reversed state. The two cells on either side of I
use the geometry and witness orientations from round 025. Coordinates depend
only on the labeled network, not on a satisfying assignment. The current
experimental constructor also accepts colors to build a test witness; removing
that computational dependency is an outstanding implementation obligation.

Each E cell retains its base induced graph at both lengths. Round 024 checks
all 256 ordered state/length pairs, and the first four junction arms have the
checked canonical coloring. Round 025 checks all four length choices around I.
Round 033 checks both endpoint junctions on a complete routed segment. Color
permutation supplies each legal endpoint pattern. Swapping the two internal
color names while fixing the signal color is included among the eight states.

## Completeness by separation

For every E orientation, normalized longitudinal projection lies in [0,1]
and absolute lateral projection is at most M=169/394. Write L=52q and U=53q.
All inequalities below are exact rational comparisons, checked in round 037.
Two nonconsecutive E cells on one straight line have point distance at least
L>2. A three-vertex path has endpoint distance at most two, so such cells
cannot both contribute to one path. Remaining interactions along a line lie
in one of the checked two-cell motifs.

At a junction, all interactions among its first four cells lie in the checked
junction. A cell beyond the first on one arm is separated from every cell on
an orthogonal arm by at least L-MU>2, using projection onto the first arm.
The corresponding bound for an opposite arm is at least L. Therefore no
three-vertex path can combine a remote cell with a different junction arm.

Relative to I's left terminal, let its extreme longitudinal coordinates be
a and b. They satisfy L+a>2 and L+27q-b>2. Thus I is more than two away from
all but the nearest E cell on either side. Its two wire sides are separated
by 27q>2. All remaining interactions occur in the checked connector. Its
position after thirteen cells separates it from endpoint junctions.

Every primitive is contained within distance U of its underlying segment or
junction. Unrelated grid features have distance at least S; after thickening,
their distance is at least S-2U>2. A monochromatic induced P3 must consequently
lie in one of the checked local motifs. The canonical local witnesses agree
at all shared signal vertices and yield a valid global three-subcoloring.

## Soundness and bounds

Restrict any valid geometric coloring to each induced primitive. The finite
forcing lemmas make E's terminals equal and I's terminals different. Equality
along each wire recovers its endpoint relation, and the junction forces all
incident ports to agree. Reading central junction vertices therefore returns
a satisfying assignment of H from every valid target coloring.

A k-unit segment uses 29k-2 free E cells and at most one I. Junctions have
constant size. If H has v vertices and total grid length ell, the output has
O(v+ell) vertices. All primitive denominators are fixed constants, so a grid
box of side B needs O(log(B+2)) bits per output coordinate. Straightforward
exact construction is polynomial in the explicit network and its total grid
length. A binary-coded arbitrary long segment would not satisfy that premise;
the source crossbar uses a constant-size template in every cell.

## Scope

The finite base forcing facts have Z3 and independently encoded CP-SAT support.
This argument and its interaction classification have not received independent
author review. The six saved source networks satisfy the geometric premises,
and the fixed template and cell gluing give a proposed all-input argument.
Executable construction without a coloring oracle, complete source-level
geometric tests, and independent review remain necessary for a campaign result.
