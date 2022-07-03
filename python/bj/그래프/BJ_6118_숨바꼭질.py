import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N+1)}

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = [False] * (N + 1)
visited[1] = True
temp_level = []
level = 0
cnt = 1

while q:
    temp = []
    if cnt == N:
        break
    level += 1
    for _ in range(len(q)):
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                temp.append(next)
                q.append(next)
                cnt += 1
    temp_level = list(temp)
temp_level.sort()
print(temp_level[0], level, len(temp_level))