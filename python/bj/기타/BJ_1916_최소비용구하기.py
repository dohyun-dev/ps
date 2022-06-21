import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict
from heapq import heappush, heappop

N, M = int(input()), int(input())   # 도시의 개수
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

q = []
dist = [sys.maxsize] * (N + 1)
dist[start] = 0
heappush(q, (0, start))

while q:
    cost, cur = heappop(q)
    if cost > dist[cur]:
        continue
    for next, next_cost in graph[cur]:
        if dist[next] > cost + next_cost:
            dist[next] = cost + next_cost
            heappush(q, (dist[next], next))

print(dist[end])