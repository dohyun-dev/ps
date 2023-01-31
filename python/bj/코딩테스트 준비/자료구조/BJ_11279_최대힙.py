from heapq import heappush, heappop

N = int(input())
q, answer = [], []

for _ in range(N):
    x = int(input())
    heappush(q, -x)

    if x == 0:
        answer.append(str(-heappop(q)))

print("\n".join(answer))