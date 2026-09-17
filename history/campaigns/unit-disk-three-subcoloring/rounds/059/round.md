# Round 059 — inspectable finite forcing kernels

## Plan

Extract an unsatisfiable core of induced-P3 constraints for each forbidden
terminal relation of the 35-vertex E and I gadgets. Use mature Z3 tracked
assertions, with color domains and pinned terminal colors explicit. The
finite scope is two core extractions and at most 100 greedy deletion checks
per core. Independently replay each retained kernel with CP-SAT after checking
that every listed triple is an actual induced P3 in the rational graph.
The aim is a smaller inspectable proof obligation for soundness, not a new
gadget. A core is still a finite computational certificate; solver agreement
alone is not a human proof or novelty evidence. Completion: two kernels and
independent infeasibility checks, with actual constraint/query counts.
Experience: round 052 shows universal soundness depends on these local
necessary relations, so reducing this obligation is directly relevant.

## Evidence and diagnosis

The E kernel decreases from 1,041 P3 constraints to 658; the I kernel from
1,050 to 692. Each is independently CP-SAT INFEASIBLE under its stated
forbidden terminal colors. The round used 202 Z3 queries and two CP-SAT
queries, with 100 deletion attempts per kernel. See [output.jsonl](output.jsonl),
[eq-kernel.json](eq-kernel.json) and [ne-kernel.json](ne-kernel.json), generated
by `python3 rounds/059/probe.py` from the campaign directory. No repairs or
reruns. The kernels remain too large to count as concise human proofs; no
minimality or independently checked formal proof trace is claimed.
Experience extraction: extend the pending composition finding with these
finite forcing obligations and their size limit; do not promote solver
agreement to publication-level mathematical review. Shared writes blocked.
Next: use the last allocated round to challenge recovery with target
colorings outside the clean canonical search domain.
