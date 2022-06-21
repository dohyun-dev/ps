import sys; input = lambda : sys.stdin.readline().rstrip()

v, e = map(int, input().split())
graph = [[sys.maxsize] * (v + 1) for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = sys.maxsize
for i in range(1, v+1): answer = min(answer, graph[i][i])
print(-1 if answer == sys.maxsize else answer)