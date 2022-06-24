import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

q = []
result = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if q:
            result.append(str(heappop(q)[1]))
        else:
            result.append("0")
    else:
        heappush(q, (abs(x), x))
print("\n".join(result))
