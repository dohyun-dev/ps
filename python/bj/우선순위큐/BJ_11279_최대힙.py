import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

q = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if q:
            print(-heappop(q))
        else:
            print(0)
    else:
        heappush(q, -x)