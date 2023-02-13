from collections import deque

def bfs(node):
    q = deque([node])
    visited = [False] * (N + 1)
    visited[node] = True
    cnt = 1
    while q:
        node = q.popleft()
        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                cnt += 1
                q.append(next)
    return cnt

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
answer = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for node in range(1, N+1):
    answer[node] = bfs(node)

max_value = max(answer)
for i in range(1, N+1):
    if max_value == answer[i]:
        print(i, end=" ")