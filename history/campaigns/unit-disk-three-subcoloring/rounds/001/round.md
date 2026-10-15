# Round 001 — pair relations in the half-integer grid

## Plan

Hypothesis: some induced subgraph of the 4-by-4 half-integer grid, with at most
ten vertices, can force two terminals to agree or differ in every legal
three-subcoloring. Such a relation could support palette and wire interfaces;
clause semantics and geometric composition would still be missing.

First test the full 16-vertex grid: for all 120 terminal pairs, ask for both
agreement and disagreement. If both extend to full-grid colorings, restriction
to any vertex subset proves no induced subgraph in this grid can force a pair
relation. This hereditary shortcut covers the proposed family without running
a solver on every subset. Scope: one grid, 240 constrained queries; stop after
these queries. Exact rational geometry, Z3, no timeout.

Relevant experience search: `subcolor|palette|unit.disk|universal.vertex` found
no matching shared entry. Use the question's universal-vertex obstruction;
this experiment changes to local rather than universal attachments.

## Evidence and diagnosis

Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/001/probe.py`.
[Raw output](output.jsonl): all 240 constrained queries are SAT; all 240 returned
colorings pass the independent component checker. One geometric template,
120 terminal pairs, zero source instances and zero recovery calls.

Every pair can agree and can differ in the full grid. Restricting each witness
proves this for every induced subgraph containing that pair, including every
subset of at most ten vertices. This is a finite-family exclusion by a general
restriction argument, not a universal impossibility result. The cause of failure
is excess coloring freedom, established for this grid. No repair or rerun.
Time/token usage: not measured.

Experience extraction: one proposed entry pending at
`research/experience/hereditary-terminal-extension.md` because this campaign's
user-supplied write scope restricts changes to the campaign. Claim: if every
terminal assignment in a specified relation extends to a full host graph,
restriction excludes any stricter terminal relation on its induced subgraphs.
Evidence: the 240 checked witnesses here. Review: main-agent only.

## Next action

Reconsider the geometric host before synthesizing gadgets. Test a finite set of
denser and larger square grids for the existence of any three-color obstruction.
This addresses whether the oracle can distinguish geometric NO instances and
whether this family can supply nontrivial constraints. Short-term prospects
remain unknown; this one host supplies no pair-forcing mechanism.
