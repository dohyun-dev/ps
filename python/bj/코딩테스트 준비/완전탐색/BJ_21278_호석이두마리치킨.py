from itertools import combinations
from collections import deque

def bfs(start, shops):
    q = deque([(start, 0)])
    visited = [False] * (N+1)
    visited[start] = True

    while q:
        cur, distance = q.popleft()

        if cur in shops:
            return distance

        for next in roads[cur]:
            if not visited[next]:
                q.append((next, distance + 1))
                visited[next] = True

N, M = map(int, input().split())
roads = {i: [] for i in range(1, N+1)}
answer = float("inf")
answer_list = []

for _ in range(M):
    a, b = map(int, input().split())
    roads[a].append(b)
    roads[b].append(a)

for combi in combinations(range(1, N+1), 2):
    distance = 0
    for i in range(1, N+1):
        distance += bfs(i, combi) * 2
    if distance < answer:
        answer = distance
        answer_list = combi

print(answer_list[0], answer_list[1], answer)