import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(node):
    global answer
    visited[node] = True
    answer += 1
    for next in graph[node]:
        if visited[next]:
            continue
        DFS(next)

N, M = int(input()), int(input())
visited = [False] * (N + 1)
graph = {i: [] for i in range(1, N+1)}
answer = -1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
DFS(1)
print(answer)


