# Sparse witnesses for compressed variable declarations

Tags: Karp reduction, witness recovery, bit complexity, unused variables, sparse assignment.

## Claim and applicability

If a source declares n variables using a binary or decimal integer, an empty
formula can have O(log n) input length. Requiring recovery to emit n Boolean
entries is not polynomial in that input when the target witness is small.
A sparse assignment with a fixed default value avoids this mismatch: only
mentioned variables need entries. Explicit integer numerator/denominator
encodings likewise avoid exponential compression through coordinate exponents.
This concerns encoding contracts, not satisfiability or hardness of a new problem.

## Evidence and status

The length lower bound is immediate for the empty formula. The repair and
executable 5,001-digit declaration regression are in
[round 006](../../campaigns/depth-three-unit-two-interval/rounds/006/round.md).
The recovered source witness occupies 18 JSON bytes for that case. The maps
also pass the nine-case extended loop with two 10^30 declarations.
The subsequent [independent review](../../campaigns/depth-three-unit-two-interval/reviews/independent/review.md)
checked the bit bounds and exercised recovery on a separately constructed
nonempty witness with a 10^100 variable declaration. These tests do not certify
all recovery algorithms or every proposed compressed-witness format.

## Consequence for search

State the actual input and witness encodings before claiming bit-polynomial
recovery. Use a sparse witness when unused labels are compressed; do not repair
an exponential output obligation merely by declaring that n counts as input size.
If the question truly requires a dense witness, its input encoding must support
that output length. Keep arbitrary-precision parsing from imposing an unrelated
fixed digit ceiling on a claimed all-input algorithm.

## Use history

No subsequent campaign use yet. On 2026-09-16,
[Unanimous Vote screening](../open-problems/nonuniform-cost-unanimous-vote.md)
used the explicit-encoding check to flag exponential denominators in a proposed
probability construction. This prevented accepting that encoding without a
gap-preserving replacement; it did not yield a reduction or measure comparative
discovery benefit.
