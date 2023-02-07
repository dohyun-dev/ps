from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)
parent = [0] * (N + 1)
visited = [False] * (N + 1)
q = deque()

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q.append(1)
visited[1] = True

while q:
    cur = q.popleft()
    for next in graph[cur]:
        if visited[next]:
            continue
        parent[next] = cur
        visited[next] = True
        q.append(next)

print("\n".join(str(parent[i]) for i in range(2, N+1)))
