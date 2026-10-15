# Manuscript consistency addendum

Date: 2026-09-16. Scope: editorial consistency of `work/manuscript.typ` with
`review.md`; no executable checks rerun and no candidate or test changes.

**Assessment: the advance decision stands. One mathematical wording correction
is needed before final rendering.**

At `work/manuscript.typ:110–111`, the interval `(394/29,394/25]` concerns
**squared** terminal spans. The sentence currently says the spans `50q`,
`(103/2)q`, and `52q` themselves lie in that interval; this is numerically false.
Replace it with: “The squares of the spans `50q`, `(103/2)q` and `52q` lie in
this interval.” The preceding sentence, implementation, and independently
checked scaling claims already use the correct squared-distance condition.
This correction does not change the construction or require experiments.

Lemma 4 includes the reviewed junction argument, the 96 orientation/relation
separation cases, full endpoint hubs, and the fixed internal-boundary strip.
It correctly separates the all-length argument from the supplementary checks
on three- through five-unit wires. I found no material mismatch in its locality
reasoning or in the universal recovery argument.

The abstract, finite-forcing proof, limitations, and appendix consistently call
the result computer-assisted, disclose reliance on solver implementations,
distinguish constraint kernels from formal UNSAT proof traces, and preserve the
partial-oracle and literature-coverage limitations. Reported independent-check
counts match the reviewed evidence. Figure descriptions distinguish exact
primitive/clause data from the schematic wire skeleton; visual rendering itself
was outside this text-consistency check. The stale contract status is corrected.

No new mathematical strategy or research round is requested. Once the squared-span
wording is corrected, no further manuscript-consistency issue remains from this
focused review; normal final rendering and visual inspection can proceed.
