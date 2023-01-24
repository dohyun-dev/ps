from itertools import combinations
from collections import deque

def bfs(shops):
    q = deque()
    visited = [False] * (N+1)
    total = 0

    for shop in shops:
        q.append((shop, 0))
        visited[shop] = True

    while q:
        cur, distance = q.popleft()

        for next in roads[cur]:
            if not visited[next]:
                q.append((next, distance + 1))
                visited[next] = True
                total += distance + 1

    return total * 2

N, M = map(int, input().split())
roads = {i: [] for i in range(1, N+1)}
answer = float("inf")
answer_list = []

for _ in range(M):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

for combi in combinations(range(1, N+1), 2):
    distance = bfs(combi)
    if distance < answer:
        answer = distance
        answer_list = combi

print(answer_list[0], answer_list[1], answer)