# Verification status

The compact candidate in `algorithm.py` uses the round 051 network and geometry
modules. Actual full-source YES and NO decisions now have certificate-assisted
checks. General correctness and novelty have not received independent review.

| Scope | Evidence | Result |
|---|---|---|
| Original small oracles | [040](../history/campaigns/unit-disk-three-subcoloring/rounds/040/self-test.json) | 228 graph-oracle comparisons and six source cases; unchanged definitions |
| Wider primitive composition | [042](../history/campaigns/unit-disk-three-subcoloring/rounds/042/output.jsonl), [043](../history/campaigns/unit-disk-three-subcoloring/rounds/043/output.jsonl) | 256 pairs and 16 inequality connectors pass |
| Rational detour composition | [048](../history/campaigns/unit-disk-three-subcoloring/rounds/048/output.jsonl), [049](../history/campaigns/unit-disk-three-subcoloring/rounds/049/output.jsonl), [050](../history/campaigns/unit-disk-three-subcoloring/rounds/050/output.jsonl) | 72 segments, 81 stars and 72 support certificates pass |
| Full candidate-provided witness | [051](../history/campaigns/unit-disk-three-subcoloring/rounds/051/output.jsonl) | Actual positive-unit output and six recoveries pass; not independently searched |
| Independent full YES search | [052](../history/campaigns/unit-disk-three-subcoloring/rounds/052/output.jsonl), [053](../history/campaigns/unit-disk-three-subcoloring/rounds/053/output.jsonl) | 537,397 vertices, 15,813 induced copies checked, two phase queries, six fresh recoveries |
| Independent full NO certificate | [054](../history/campaigns/unit-disk-three-subcoloring/rounds/054/output.jsonl) | Actual 1,547,820-vertex opposite-unit target is NO |
| New oracle self-checks | [055](../history/campaigns/unit-disk-three-subcoloring/rounds/055/output.jsonl) | 516 geometric comparisons, 5,422 coloring-predicate comparisons, seven malformed cases, four numeric-bound cases and empty target |
| Broader source injection | [056](../history/campaigns/unit-disk-three-subcoloring/rounds/056/output.jsonl) | All six prepared cases pass across rounds 053/054/056: four YES, two NO, 24 recoveries |

The target oracle treats the supplied primitive-index manifest as untrusted.
It computes every listed induced graph from actual rational centers before
using the independently solved necessary terminal relations. Projection UNSAT
certifies target NO. Projection SAT is explicitly unknown until the second
search finds a complete coloring whose monochromatic components are cliques
in the whole exact graph. Restricted-domain search UNSAT is never target NO.

The oracle searches permutations of validated local colorings using Z3. The
whole-graph predicate supplies excluded assignments from actual P3s. Successful
witnesses come from this separate program, and recovery runs in a fresh
candidate process. These are separately implemented programs by the same main
author, not an independent agent or human review.

The new exact-neighbor implementation uses bounded exactly representable
integer coordinates and checked int64 distance products. Unsupported numeric
ranges fail explicitly. Its partial-solver scope is documented in rounds
052--055; no complete general-purpose target decision algorithm is claimed.

The first round 054 certificate producer omitted inequality copies. The oracle
correctly returned unknown. The producer was repaired and rerun on the unchanged
actual target; failed artifacts remain beside the successful evidence. No
reduction counterexample was inferred from that producer defect.

Both reusable commands now pass on the unchanged round 051 candidate:

- `python3 work/check.py --candidate work/algorithm.py` — all six prepared
  sources agree, with 19 fresh-process recoveries; [raw log](../history/campaigns/unit-disk-three-subcoloring/rounds/060/prepared-suite.jsonl).
- `python3 work/verify.py --candidate work/algorithm.py` — two additional
  sources with 5,001-digit declarations and labels agree, seven recoveries,
  six malformed-source checks; [raw log](../history/campaigns/unit-disk-three-subcoloring/rounds/060/additional-verification.jsonl).
- `python3 work/check.py --self-test` — [current result](../history/campaigns/unit-disk-three-subcoloring/rounds/060/integrated-self-test.json).

Commands above are relative to the campaign directory. Evidence directories
refuse overwrite; subsequent runs must choose a fresh `--evidence` path.
Integration did not change either candidate map. The harnesses share the
large-target oracle; their passes are not independent implementations of it.
Round 060 also supplies eight noncanonical full-witness modifications with
successful recovery, beyond the restricted template search domain. Their
fixed-exterior scope is explicit in the round record.

The general finite-neighborhood proof and all-input recovery require native
independent review. No advance verdict or publication manuscript exists.
