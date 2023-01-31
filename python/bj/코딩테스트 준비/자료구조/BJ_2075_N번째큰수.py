from heapq import heappush, heappop, heapify

N = int(input())
arr = [[*map(int, input().split())] for _ in range(N)]
q = [*arr[0]]
heapify(q)

for i in range(1, N):
    for j in range(N):
        heappush(q, arr[i][j])
        heappop(q)
print(heappop(q))