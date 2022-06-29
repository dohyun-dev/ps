import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

for _ in range(int(input())):
    input()
    q = []
    result = 0
    for i in map(int, input().split()):
        heappush(q, i)

    while len(q) >= 2:
        temp = heappop(q) + heappop(q)
        result += temp
        heappush(q, temp)
    print(result)


