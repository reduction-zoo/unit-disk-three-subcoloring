# Round 004 — repair the replication premise

## Plan

Test whether reducing independent bag size to two or three, or making replicated
bags cliques, preserves the proper-coloring converse while avoiding round 003's
obstruction. Scope: source K4, independent bag sizes 1,2,3,4, and the general
lemma for arbitrary nonempty clique substitution. Check the four finite graphs
with the prepared oracle; reason about clique substitution for all inputs.
If every variant fails logically or geometrically, stop this route rather than
optimizing coordinates. Shared search for `twin|replicat|clique.*substitut` will
be checked; use round 003's pending obstruction locally.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/004/probe.py`.
[Raw output](output.jsonl): K4 expanded by one, two, or three independent twins
is three-subcolorable; four twins are not. Explicit witnesses assign color r
to replica r in every bag when the bag size is at most three. Each color class
is then a clique across the bags. Thus source K4 is a NO proper-coloring
instance that becomes a YES target, refuting each smaller replication converse.
Four templates and four solver queries; no 3-SAT or full-rule extraction calls.
No rerun; usage unavailable. Keyword matches in shared experience concern L1,
queue layouts, and matching cuts, with different premises; none applies.

General true-twin lemma: replacing each vertex by a nonempty clique and each
edge by a complete join leaves the subchromatic number unchanged. Restricting
to one representative proves one inequality. Extending each source color to
its entire bag preserves clique components and proves the other. Therefore
adjacent replication cannot turn subcoloring into proper coloring. This also
covers arbitrary bag sizes; no coordinate search can repair that semantic gap.

Experience extraction: update the pending replication entry from round 003
with the smaller-bag K4 counterexamples and true-twin invariance. Still one
pending entry for this route, not one per round. Main-agent proofs only.

## Next action

Stop complete-join replication. Return to geometric constraints, but replace
regular grids by explicitly bounded irregular point samples. This is justified
by the unresolved possibility that grid symmetry hides four-color obstructions;
the check is diagnostic rather than evidence that a full reduction is near.
