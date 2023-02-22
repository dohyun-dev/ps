from collections import deque

def bfs(start, end, pre_nodes=set()):
    q = deque([(start, 0, [start])])
    visited = [0] * (N + 1)
    visited[start] = start

    while q:
        node, cnt, pre = q.popleft()

        if node == end:
            return [cnt, pre[1:-1]]

        for next in graph[node]:
            if visited[next] or next in pre_nodes:
                continue
            visited[next] = node
            q.append((next, cnt+1, pre+[next]))

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

S, E = map(int, input().split())

for v in graph.values():
    v.sort()

start_route = bfs(S, E)
end_route = bfs(E, S, set(start_route[1]))
print(start_route[0] + end_route[0])