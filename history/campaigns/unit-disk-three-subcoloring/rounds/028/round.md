# Round 028 — executable 3-SAT to proper three-coloring

## Plan

Assemble the verified GJS clause graph with a palette triangle, paired literal
vertices, and output-to-false/base edges. Implement witness recovery by comparing
each positive literal color with the true palette color. Test all formulas of
at most two clauses on one variable (45 formulas), all one-clause formulas on
two variables (64), and the eight-clause two/three-variable blocking examples
explicitly listed by the script. Use the independent prepared source solver
and independent proper-color constraints, then check six color permutations
of every returned YES witness. This tests known source compilation only;
unit-disk mapping and full bit bounds remain separate obligations.
Experience: reuse the round 027 transcription checks, not an unsupported new
clause gadget. No matching shared source-compiler finding was located.

## Evidence and diagnosis

All 112 source cases agree with the independent source solver: 110 YES
and 2 NO. The extractor passes 660 color-permuted recovery checks.
These are proper-color graph targets, not the fixed unit-disk targets.
Counts: 224 solver queries, 112 intermediate source injections; zero complete
unit-disk injections or recovery calls. No repairs. Time/token unavailable.
Command: `python3 campaigns/unit-disk-three-subcoloring/rounds/028/probe.py`;
raw evidence: [output.jsonl](output.jsonl).

The source compiler is linear in n+m but n is binary in the temporary JSON
contract. Unused declared variables therefore require an encoding audit before
claiming input-bit polynomial bounds. This does not affect the finite tests.
Experience extraction: none new; known source construction validated.
Next test a direct geometric crossing before engineering a planarized macro.

### Encoding repair (not another research round)

Retrieved [compressed-variable-declarations](../../../../research/experience/compressed-variable-declarations.md)
and its round 006 evidence after identifying the bit-size gap. The fixed
question does not require a dense JSON witness. Replace that temporary witness
encoding with a sparse assignment, false by default, and allocate only mentioned
variables in the source oracle/compiler. This represents the same assignment
and preserves both decision languages. Dense files and original results are
preserved under `dense-*`; the updated probe adds two compressed-declaration
cases, including 5,001 decimal digits. This is an oracle/encoding repair, not
a new construction family or a counted research round.

Experience extraction: the existing compressed-variable entry now has a
qualifying use-history update pending at the shared destination. Its exact
premise prevented a false bit-polynomial claim here. No shared file was edited
under the campaign-only scope. This is a sixth distinct pending destination.

Sparse repair outcome: 114 intermediate cases pass, including both
compressed declarations; 672 intermediate recoveries pass.
The complete oracle self-test passes in [sparse-self-test.json](sparse-self-test.json).
This adds 228 source/intermediate solver queries. Full unit-disk source
injections remain zero. An administrative count script needed Python's integer
string limit disabled to read the 5,001-digit saved case; no experiment reran.
