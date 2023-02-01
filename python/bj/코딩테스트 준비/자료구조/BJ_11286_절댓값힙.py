from heapq import heappush, heappop

N, q, answer = int(input()), [], []
for _ in range(N):
    num = int(input())
    if num != 0:
        heappush(q, (abs(num), str(num)))
    else:
        if q:
            answer.append(heappop(q)[1])
        else:
            answer.append('0')
print("\n".join(answer))