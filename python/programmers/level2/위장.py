from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter(b for a, b in clothes)
    return reduce(lambda a, b: a * (b + 1) ,counter.values(), 1) - 1