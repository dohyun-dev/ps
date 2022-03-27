import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
indegree = [0] * (N + 1)

for _ in range(M):  
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
q = deque([i for i in range(1, N+1) if indegree[i] == 0])

result = []
while q:
    cur = q.popleft()
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
    result.append(str(cur))
print(*result)