from collections import deque

def dfs(node):
    stack = [node]
    visited = [False] * (N + 1)
    answer = []

    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        answer.append(str(cur))
        visited[cur] = True
        stack.extend(graph[cur][::-1])

    print(" ".join(answer))

def bfs(node):
    q = deque([node])
    visited = [False] * (N + 1)
    answer = []

    while q:
        cur = q.popleft()
        if visited[cur]:
            continue
        answer.append(str(cur))
        visited[cur] = True
        q.extend(graph[cur])

    print(" ".join(answer))

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for v, e in graph.items():
    e.sort()
dfs(V)
bfs(V)