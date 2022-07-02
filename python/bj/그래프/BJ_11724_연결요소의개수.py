import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def bfs(cur):
    q = deque([cur])
    visited[cur] = True

    while q:
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)


N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    if not visited[i]:
        bfs(i)
        cnt += 1
print(cnt)