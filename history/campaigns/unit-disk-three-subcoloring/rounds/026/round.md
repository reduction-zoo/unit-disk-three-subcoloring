# Round 026 — planar source compilation from primary literature

## Plan

Read the original Garey--Johnson--Stockmeyer 1976 planar three-coloring
construction, including crossover and degree restrictions. The finite scope
is that paper and at most two academic expositions of its diagrams. Determine
an explicit composition from 3-SAT, polynomial embedding and universal recovery.
This uses round 025's geometric edge interface; a complete source compiler is
still missing. No solver experiment is declared in this literature round.
Existing shared experience search yielded no matching planar compiler; the
local terminal-composition finding remains relevant only to the later geometry.

## Evidence and diagnosis

Inspected Garey, Johnson and Stockmeyer, *Some simplified NP-complete graph
problems* (1976), Theorems 2.1--2.3, printed pages 248--251, Figures 1--3.
Primary source: https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/JohnsonDavid2.pdf
DOI: https://doi.org/10.1016/0304-3975(76)90059-1
Search/inspection date: 2026-09-16. The local source PDF and rendered pages
preserve the inspected diagrams. No secondary exposition was needed.

Theorem 2.1 supplies a six-internal-vertex clause gadget with a distinguished
output, completing the ordinary 3-SAT-to-three-coloring reduction. Theorem 2.2
gives a 13-vertex planar crossover: opposite ports have equal colors, and all
nine ordered pairs of crossing signals extend. The construction uses one
inequality edge per original edge and equal propagation along the remainder.
These statements directly support universal recovery by restricting colors to
original vertices, then comparing variable colors with the palette. A diagram
transcription must still be tested independently of the printed assertion.

Theorem 2.3 bounds proper graph degree by four, but geometric compilation can
instead split each high-degree vertex into a planar equality cycle. This uses
the actual equality primitive and avoids adding unnecessary color gadgets.
No algorithm for the complete geometric map was implemented in this round.
Counts: one primary paper inspected, zero solver queries, source injections or
recovery calls. Time/token usage unavailable.

Experience extraction: none new; the source construction is published work.
It supplies a justified compiler route, not a new result. Next transcribe and
exhaustively check the two constant gadgets before committing to routing.
