# Round 060 — recovery beyond canonical local colorings

## Plan

Keep the actual positive-unit target and its independently found full witness.
Select four E copies spread through the manifest and four I copies spread
through it. For each, allow all 35 vertex colors to vary while fixing every
other vertex. Solve all affected actual P3 constraints with Z3 in two modes:
(1) require a local coloring outside all six permutations of the saved clean
primitive coloring; (2) require a terminal to have a same-color neighbor.
This is 16 queries with a fixed exterior, not enumeration of all target
witnesses. Independently recheck all affected P3s in every returned witness,
then run fresh-process recovery and validate the original formula. Unaffected
P3s retain the already validated exterior coloring. UNSAT excludes only that
selected fixed-exterior local modification. Completion: 16 statuses and all
successful recovery calls, or a concrete counterexample. Experience: necessary
local forcing supports universal recovery without a cleanliness assumption;
this round tests whether the implemented recovery silently relies on one.

## Evidence and diagnosis

All 16 queries completed. Eight noncanonical local modifications are SAT;
every resulting full witness passes its complete affected-P3 check and
fresh-process source recovery. The eight nonclean queries are UNSAT only
under their fixed exteriors; no global cleanliness theorem is inferred.
See [output.jsonl](output.jsonl) and the eight saved patch/recovery files.
Command: `python3 rounds/060/probe.py` from the campaign directory. Sixteen
Z3 queries, eight recovery calls, no repairs or reruns. This provides evidence
beyond the restricted canonical template domain used by the large YES oracle.
Experience extraction: extend pending geometric-composition/projection entries
with this limited unrestricted-color test and its exact fixed-exterior scope.
Shared writes remain blocked. Twenty additional rounds are complete, totaling
60. Finish ordinary verification integration and independent review of this
unchanged candidate without charging a new discovery round; substantive
mathematical revisions would need a new allocation.

## Verification integration after the allocation

The unchanged candidate passes the integrated prepared and additional
verification commands. The current self-test, `prepared-suite.jsonl` and
`additional-verification.jsonl` preserve the actual outputs. All six prepared
sources pass with 19 recovery calls; two 5,001-digit active-variable sources
pass, with seven recoveries including the empty case and six malformed-source
checks. This integration used 19 and six solver queries respectively, excluding
oracle self-tests. Both harnesses share the previously checked large-target
oracle; that common dependency is explicit in the stage reports.
No additional construction hypothesis or research round was introduced.
Native independent review is the next responsibility for this candidate.


## Post-allocation review and writing closeout

No new research round was started. The native independent review in
`../../reviews/compact-construction/review.md` gives advance after its own
forcing, source, routing and 96-case cross-arm separation checks. The review
supplies the mixed-direction locality elaboration for the existing construction.
Its manuscript consistency addendum requests only a squared-span wording
correction, which is applied. The submitted development proof is preserved
as `submitted-proof.md`; its status was updated after review.

The native English `../../work/manuscript.typ` and `report.typ` compile to an
8-page PDF with three SVG figures generated from exact graph data and an
explicit wire skeleton. Initial inspection found an overwide coordinate display,
duplicated figure-reference prefixes and a separated equation setup. These
editorial defects were repaired; all eight initial pages and affected final
pages were inspected. The final compile command, from the repository root, is:

```
typst compile campaigns/unit-disk-three-subcoloring/work/manuscript.typ campaigns/unit-disk-three-subcoloring/work/manuscript.pdf
```

It exits successfully with no diagnostics. Raster inspection uses `pdftoppm
-scale-to 1100 -png` and the saved page images in `work/figures/`.
The initial optional matplotlib figure attempt failed because that package was
not installed; the finished generator uses only the standard library and does
not add a dependency. No mathematical checks needed rerunning for these edits.
Bibliographic metadata for arXiv:2604.26533 and the authors of DOI
10.1016/j.comnet.2026.111990 were verified against arXiv and the publisher's
abstract page on 2026-09-16 during writing; the full-text coverage gap remains.

Experience closeout remains 0 shared files created, 0 updated, and 7 pending
destinations under the campaign-only write scope. The independent locality
check strengthens the existing terminal-composition destination rather than
creating an eighth entry. All evidence remains in this campaign.
