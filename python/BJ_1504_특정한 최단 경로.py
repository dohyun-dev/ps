import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict
from heapq import heappush, heappop

def dijksta(start, graph):
    dist = [sys.maxsize] * (N + 1)
    dist[start] = 0
    q = []
    heappush(q, (0, start))
    
    while q:
        cost, cur = heappop(q)
        
        if dist[cur] < cost:
            continue
        for next, next_cost in graph[cur]:
            temp = cost + next_cost
            if dist[next] > temp:
                dist[next] = temp
                heappush(q, (dist[next], next))
    return dist

N, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

from_1 = dijksta(1, graph)
from_v1 = dijksta(v1, graph)
from_v2 = dijksta(v2, graph)

# 1 -> v1 -> v2 -> N
dist1 = from_1[v1] + from_v1[v2] + from_v2[N]

# 1 -> v2 -> v1 -> N
dist2 = from_1[v2] + from_v2[v1] + from_v1[N]

answer = min(dist1, dist2)

if answer < sys.maxsize:
    print(answer)
else:
    print(-1)
