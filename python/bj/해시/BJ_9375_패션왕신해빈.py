import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict
from functools import reduce

for _ in range(int(input())):
    N = int(input())
    closet = defaultdict(list)
    for _ in range(N):
        a, b = tuple(input().split())
        closet[b].append(a)
    print(reduce(lambda x, y: x * (y + 1), [len(l) for l in closet.values()], 1) - 1)