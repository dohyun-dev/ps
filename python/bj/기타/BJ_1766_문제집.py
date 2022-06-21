import heapq
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = [i for i in range(1, N+1) if indegree[i] == 0]
heapq.heapify(q)
result = []

while q:
    cur = heapq.heappop(q)
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            heapq.heappush(q, node)
    result.append(cur)
    
print(*result)