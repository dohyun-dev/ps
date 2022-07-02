import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = int(input()), int(input())
graph = {i: [] for i in range(1, N+1)}
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited[1] = True
answer = 0
level = 0
while q:
    level += 1
    if level > 2:
        break
    for _ in range(len(q)):
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                answer += 1
print(answer)