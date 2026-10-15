# Round 015 — equality diamond

## Plan

Hypothesis: five inequality gadgets around two triangles sharing an edge yield
a clean equality wire. Terminal skeleton: a=(0,0), b=(2,0), c=(1,433/250),
d=(1,-433/250). Edges ab,bc,ca,ad,db. Keep four exterior edge interiors outward;
choose either side for ab and independently reverse the five gadgets' endpoints.
Scope: up to 64 placements of 169-vertex graphs, stop at first valid clean
extension of skeleton colors (0,1,2,2). Check canonical lifting first; otherwise
ask Z3 with all four skeleton vertices clean, a sufficient condition stronger
than merely cleaning c,d. At most 64 queries. Save successful geometry.

Soundness would follow from induced local inequality copies: c and d both
avoid the distinct colors of a,b. Remaining obligations: serial and bent
composition, branching, and encoding an NP-hard source. Use rounds 012--014's
finite gadgets and pending composition finding. No timeout.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/015/probe.py`.
[Output](output.jsonl): all 64 placements fail canonical extension and all 64
queries with all four skeleton vertices clean are UNSAT. Every embedded edge
still has the correct induced local adjacency. Thus the failed condition is
in global composition, not local distortion. No rerun, source/recovery calls,
or measured usage.

The result does not establish that the diamond graphs themselves are UNSAT:
cleaning the two auxiliary vertices a,b was stronger than necessary. Before
changing geometry, distinguish this excess condition from actual infeasibility.
The fixed reduction target is unchanged by removing cleanliness at auxiliaries;
only external ports c,d need that sufficient gluing condition.

Experience extraction: none new. The global-cross-edge lesson is already in
the pending terminal-composition entry. The cause beyond failure of the stronger
condition is unresolved, so do not extract an impossibility claim.

## Next action

Recheck the same placements without auxiliary cleanliness, then require only
c,d to be clean when an ordinary coloring exists. This is the smallest check
that separates an overstrong local requirement from a geometric obstruction.
