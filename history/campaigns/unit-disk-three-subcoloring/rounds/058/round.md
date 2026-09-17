# Round 058 — novelty of the completed construction target

## Plan

Recheck whether rational unit-disk three-subcoloring hardness has been settled
by a later paper or an equivalent cluster-partition formulation. Search three
focused Web/arXiv queries covering 3-subcoloring, subchromatic number three,
and partition into three cluster graphs; inspect the original open-problem
statement and the identified 2026 follow-up. Check applicability, not just
matching titles. The claim concerns supplied rational representations and
ordinary Karp reduction from 3-SAT; arbitrary-radius disks and two colors do
not imply it. Completion: record primary URLs, locations, date, observed
scope and remaining coverage gaps. No new mathematical construction in this
round. Experience: known implication checks precede any novelty claim.

## Evidence and diagnosis

Search date: 2026-09-16. Actual initial queries:
`"unit disk" "3-subcoloring" 2026`, `"unit disk" "subchromatic" "three"`,
and `"unit disk" "three cluster graphs"`.

[Marin and Watrigant, MFCS 2025, Section 6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.74/LIPIcs.MFCS.2025.74.html)
explicitly leaves unit-disk three-subcoloring complexity open. The
[arXiv record](https://arxiv.org/abs/2506.19452) lists only v1 (2025-06-24);
its [Section 6](https://arxiv.org/html/2506.19452v1) retains that question.
Its two-color and co-comparability hardness statements do not imply this
geometric three-color target.

The [2026 follow-up](https://arxiv.org/html/2604.26533v1), Section 4.1,
Theorems 11--12 and Section 5.2, Theorem 17, concerns two colors. Its inspected
statements do not settle the fixed three-color case. The
[author's publication list](https://perso.univ-lyon1.fr/remi.watrigant/index.php?pageid=1)
also identifies a 2026 WLAN application. Follow-up queries were
`"Fair Radio Channel Assignment in WLANs via Graph Subcoloring" hardness`
and `"Fair Radio Channel Assignment" hal`.

The [publisher abstract and section snippets](https://www.sciencedirect.com/science/article/abs/pii/S1389128626000022)
describe an application algorithm, not a fixed-three recognition theorem.
Direct full-page access returned 403; the full theorem statements were not
inspected. This is a remaining coverage gap, not evidence of absence.
No resolution was located within these searches. Unindexed or unpublished
work and other cluster-partition terminology remain outside coverage.

The potential contribution remains an original rational geometric realization
of equality/inequality constraints establishing ordinary Karp hardness. The
GJS source graph and crossover are known components and are not claimed new.
Importance remains moderate within geometric graph complexity; correctness
and novelty require separate independent review. Zero solver queries.
Experience extraction: none; this updates the fixed question's dated novelty
assessment without a new reusable construction finding. Shared board edits
are outside the campaign scope. Next: produce smaller finite forcing kernels
for the two computational primitive lemmas.
