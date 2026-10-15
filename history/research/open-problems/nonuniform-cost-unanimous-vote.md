---
status: proof-route-hold
openness: extension-question-in-SOSA-2026
difficulty: uncertain
importance: moderate
tags: stochastic-testing, ordering, expected-cost, NP-hardness
last-literature-check: 2026-09-16
---

# Partition to nonuniform-cost Unanimous Vote

Screening hold. The natural expensive-test subset-selection mechanism fails
the exchange check below. No campaign or research rounds have started.

## Decision and witness contract

Source: positive binary integers a_1,...,a_m; accept if a subset sums to half
their total. A witness is the subset of indices. Target: n independent coins
with rational probabilities 0<p_i<1, positive rational costs c_i, and rational
threshold K. All rationals are explicitly binary encoded. A witness is one
permutation, fixed before seeing any outcomes. Flip in that order until both
outcomes have appeared, or all coins have been flipped. Accept if some order
has expected cost at most K.

Seek a deterministic polynomial Karp map and polynomial recovery of a source
subset from every qualifying target order. Malformed source strings can map
to a malformed target outside the language. All well-formed source instances
must yield valid probabilities and costs, including source NO instances.
The proposed output must have polynomially many coins and polynomial total
bit length; no such construction or recovery algorithm is established yet.

For an order pi, its expected cost is exactly

    c_pi(1) + sum_{k=2}^n c_pi(k)
        (product_{j<k} p_pi(j) + product_{j<k} (1-p_pi(j))).

This gives polynomial-time exact witness verification: every product uses
each input denominator at most once, and a common denominator dividing the
product of all probability and cost denominators suffices. Its bit length
is at most their summed bit lengths. The permutation uses O(n log n) bits.
Thus the proposed target is in NP. This calculation is not a hardness proof.

## Primary literature and coverage

Duman Keles, Hellerstein, Marwaha, Musco and Yang,
[An Exact Algorithm for the Unanimous Vote Problem](https://kam.mff.cuni.cz/~spring/media/papers/6/unanimousVote.pdf),
SOSA 2026, Theorem 1.1, gives an exact algorithm for unit costs. Section 7,
page 167, explicitly asks about extending to nonuniform costs. The
[full preprint](https://arxiv.org/html/2510.16678v1), Section 7, has the same
question. This wording leaves an algorithmic extension unresolved; it is not
an explicit conjecture of NP-hardness.

The earlier [ESA 2018 paper](https://www.sci.brooklyn.cuny.edu/~kletenik/publications/ESA2018.pdf),
Section 5.4 and Table 1, gives exact adaptive Unanimous Vote algorithms even
with arbitrary costs. That does not allow one fixed outcome-independent
order. Hardness for general Boolean formulas or weighted linear thresholds
does not classify the fixed not-all-equal function here.

Queries on 2026-09-16: `"Unanimous Vote" "costs" hardness`,
`"unanimous vote" "NP-hard" costs 2026`,
`"unanimous vote" "arbitrary costs"`,
`"non-adaptive" "unanimous" "cost" "hardness"`.
No later exact classification was located. The additional source trail below
addresses the initial sequential-testing coverage gap without claiming an
exhaustive literature search.
Follow-up queries `"nonadaptive" "testing" "two" "NP-hard" probabilities`,
`"non-adaptive" "not-all-equal" costs`, and
`"sequential testing" "unanimous"` returned mostly unrelated group-testing
models. They did not resolve the coverage gap; the next search should follow
the sequential-testing survey references rather than repeat these broad terms.

The same-day follow-up inspected the references in Ünlüyurt's
[2025 review](https://arxiv.org/html/2511.15742v1), Sections 2 and 4.1, then
checked the original results it cites. Gkenosis et al.,
[arXiv:2111.08793v3](https://arxiv.org/pdf/2111.08793), Sections 1–2, treats
adaptive symmetric-function evaluation and gives approximation guarantees.
Ghuge, Gupta and Nagarajan,
[arXiv:2111.05687v2](https://arxiv.org/pdf/2111.05687), Theorem 1.1 and
Section 1.1, gives a constant-factor nonadaptive approximation for score
classification. Taking unit score weights and classes {0}, {1,...,n-1}, {n}
matches the stopping rule here for n>=2, but an approximation does not decide
an arbitrary exact threshold. Neither inspected result supplies the proposed
hardness reduction or an exact nonuniform-cost algorithm. The 2022 NSF PDF
failed to load; its arXiv version was inspected instead. The attempted v4 HTML
for the other paper failed; the available PDF identifies itself as v2.

Additional queries were `Ünlüyurt 2025 sequential testing survey Boolean functions`,
`"The stochastic boolean function evaluation problem for symmetric boolean functions" pdf`,
and `Ghuge Gupta Nagarajan nonadaptive stochastic score classification arxiv`.
The current openness assessment is provisional within these sources and the
recorded 2026 searches. Uninspected older application literature remains a
coverage limit.

## Bounded analytical check: an expensive test cannot select a subset

The proposed mechanism places a distinguished expensive test s after an
unknown subset of item tests. Its reach probability would encode that subset.
Check this idea when item costs are one and p_i lies in [delta,1-delta].

After a nonempty prefix, write A for the probability of all heads and B for
the probability of all tails. Swapping adjacent tests i,j changes expected
cost by

    Cost(i,j) - Cost(j,i)
      = A [c_i(1-p_j)-c_j(1-p_i)]
        + B [c_i p_j-c_j p_i].

The continuation after both tests is identical in the two orders. If j=s
and c_s=M>=1/delta, both bracketed terms are nonpositive. Since 0<p_s<1,
they are strictly negative under these bounds. Thus any item following s
can be swapped ahead of it with strictly lower cost. At the first two
positions both tests are always executed, so their order has equal cost.
Consequently an optimum exists with s last: move a first-position s to
second at no cost, then apply the strict exchanges.

For n>=3 and all probabilities strictly interior, an order with s before
an item beyond the first-position swap cannot be optimal. The intended
variable subset before a dominant expensive test is therefore unavailable
in this family. This is an elementary screening derivation, not an
independently reviewed theorem or an exclusion of all nonuniform-cost routes.

A separate encoding obstacle affects the tempting choice
p_i=2^{a_i}/(1+2^{a_i}): its explicit denominator needs a_i+1 bits, which is
not polynomial in the binary length of a_i. Replacing it by a rational
approximation requires a proved separating gap; none has been supplied.
The shared [encoding experience](../experience/compressed-variable-declarations.md)
motivates checking explicit output length, although its original application
concerns variable declarations rather than probabilities.

## Assessment and next action

### Follow-up scope declared on 2026-09-16

Check a possible tractability obstruction for constructions using only a fixed
number t of distinct probabilities. Compare a count-state dynamic program with
independent outcome enumeration on every labeled four-coin instance with
probabilities in {1/4,3/4} and costs in {1,2,3}: 1,296 instances, 24 orders and
16 outcomes per order. This is an additional screening probe, not a campaign.
Run from the repository root:

```sh
python3 research/evidence/unanimous-vote-probability-types.py > research/evidence/unanimous-vote-probability-types.json
```

The proposed proof is as follows. Swapping two equal-probability coins leaves
every prefix survival probability unchanged. These probabilities are
nonincreasing with position. Therefore assigning the smaller cost to the earlier
position cannot increase the objective. There exists an optimum whose costs
within each probability type are sorted. A state k=(k_1,...,k_t) records how
many coins from each sorted list have been used. Every such prefix has survival
probability

    r(k) = product_j p_j^{k_j} + product_j (1-p_j)^{k_j},

except the empty prefix, where r(0)=1. Appending the next coin of a type adds
its cost times r(k), and leads to a state with that count increased. The
minimum over these transitions gives the optimum over all interleavings.
There are product_j(n_j+1) states and at most t transitions each. Arithmetic
has polynomial bit length in the explicit rational input. For fixed t this
is a polynomial algorithm; for variable t it need not be.

If confirmed, this excludes NP-hardness constructions using a constant number
of probability values unless P=NP, regardless of how many distinct costs they
use. This is an elementary inference for screening; no originality is claimed.

The declared probe completed: all 1,296 instances agreed, covering 31,104 orders
and 497,664 outcome evaluations. The
[raw result](../evidence/unanimous-vote-probability-types.json) records zero
mismatches. No repairs or reruns were needed. The two routines are separately
implemented in one main-agent program, not an independent author review.
Finite agreement supports the implementation; the general argument above is
the basis for the fixed-type tractability inference. No human or independent
agent review has been performed. Experience extraction: none; this screening
inference remains on the card pending review and broader applicability.

Gate 1 passes for this proposed contract. Gate 2 distinguishes the inspected
unit-cost, adaptive and approximation results. Gate 3 passes provisionally
within the updated source coverage. Gate 4 passes with moderate importance:
a positive result would classify a natural cost extension of a recently
solved ordering problem. Gate 5 is on hold: the inspected mechanisms do not
yet support a reduction. Gate 6 is not passed. Difficulty remains uncertain;
no moderate-difficulty claim is supported.

Resume construction only with a mechanism using a growing number of probability
values, a proved threshold gap and a decodable source subset. It must avoid
dominant-test forcing and uncontrolled exponential probabilities. No shared
experience file is created; retain the unreviewed analytical exclusions here.
