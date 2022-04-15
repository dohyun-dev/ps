from functools import reduce
def solution(sizes):
    return reduce(lambda x, y: x * y, [max(z) for z in zip(*[sorted(s) for s in sizes])])