from fractions import Fraction as F
from functools import cache
from itertools import permutations, product
import json


def optimum_by_types(items):
    probabilities = sorted(set(p for p, _ in items))
    costs = [sorted(c for p, c in items if p == q) for q in probabilities]
    @cache
    def visit(counts):
        if sum(counts) == len(items):
            return F(0)
        reach = F(1)
        if sum(counts):
            heads = tails = F(1)
            for p, k in zip(probabilities, counts):
                heads *= p ** k
                tails *= (1-p) ** k
            reach = heads + tails
        choices = []
        for t, k in enumerate(counts):
            if k < len(costs[t]):
                after = list(counts)
                after[t] += 1
                choices.append(reach * costs[t][k] + visit(tuple(after)))
        return min(choices)
    return visit((0,) * len(probabilities))


def optimum_by_outcomes(items):
    scores = []
    for order in permutations(range(len(items))):
        expected = F(0)
        for outcome in product((0, 1), repeat=len(items)):
            chance = F(1)
            for (p, _), bit in zip(items, outcome):
                chance *= p if bit else 1-p
            seen = set()
            spent = 0
            for i in order:
                seen.add(outcome[i])
                spent += items[i][1]
                if len(seen) == 2:
                    break
            expected += chance * spent
        scores.append(expected)
    return min(scores)


if __name__ == '__main__':
    alphabet = [(p, c) for p in (F(1, 4), F(3, 4)) for c in (1, 2, 3)]
    count = 0
    for items in product(alphabet, repeat=4):
        actual = optimum_by_types(items)
        expected = optimum_by_outcomes(items)
        assert actual == expected, (items, actual, expected)
        count += 1
    print(json.dumps({'instances': count, 'orders_per_instance': 24,
                      'outcomes_per_order': 16, 'mismatches': 0}))
