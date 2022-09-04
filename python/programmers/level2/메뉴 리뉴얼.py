from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    counter = defaultdict(int)
    max_count = {c: (0, []) for c in course}
    result = []

    for order in orders:
        for c in course:
            for combi in combinations(order, c):
                counter[''.join(sorted(list(combi)))] += 1

    for k, v in counter.items():
        if v >= 2:
            if v >= max_count[len(k)][0]:
                if max_count[len(k)][0] < v:
                    max_count[len(k)] = (v, [k])
                else:
                    max_count[len(k)][1].append(k)

    for v in max_count.values():
        result.extend(v[1])

    return sorted(result)