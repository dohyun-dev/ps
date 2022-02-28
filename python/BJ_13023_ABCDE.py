import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l, node):
    if l == 4:
        print(1)
        sys.exit()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            DFS(l+1, i)
            visited[i] = False
        

N, M = map(int, input().split())
graph = {i: [] for i in range(N)}
visited = [False] * N

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N):
    visited[i] = True
    DFS(0, i)
    visited[i] = False
print(0)