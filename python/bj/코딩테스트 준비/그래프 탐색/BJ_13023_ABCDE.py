from collections import defaultdict
import sys; sys.setrecursionlimit(10000)

def dfs(node, cnt=1):
    if cnt == 5:
        print(1)
        exit()

    for next in graph[node]:
        if visited[next]:
            continue
        visited[next] = True
        dfs(next, cnt+1)
        visited[next] = False

N, M = map(int, input().split())
graph = defaultdict(list)
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False
print(0)