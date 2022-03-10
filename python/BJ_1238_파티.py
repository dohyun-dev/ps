import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict;    from heapq import heappush, heappop

def dijkstra(start, end):
    q = []; heappush(q, (0, start))
    dist = [sys.maxsize] * (N + 1)
    
    while q:
        cost, cur = heappop(q)
        if dist[cur] < cost:
            continue
        for next, next_cost in graph[cur]:
            if dist[next] > cost + next_cost:
                dist[next] = cost + next_cost
                heappush(q, (dist[next], next))
    return dist[end]
            
        

N, M, X = map(int, input().split())
graph = defaultdict(list)
result = [0] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

for i in range(1, N):
    
