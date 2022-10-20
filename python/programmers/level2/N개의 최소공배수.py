from math import gcd
from functools import reduce

def solution(arr):
    return reduce(lambda acc, cur: acc * cur // gcd(acc, cur), arr, 1)

print(solution([2,6,8,14]))