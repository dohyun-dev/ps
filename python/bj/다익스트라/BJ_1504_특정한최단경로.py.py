import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra(start, end):
    q = [(0, start)]
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    while q:
        cur_cost, cur = heappop(q)
        
        if dist[cur] < cur_cost:    
            continue
        
        for next, next_cost in graph[cur]:
            cost = cur_cost + next_cost
            if cost < dist[next]:
                dist[next] = cost
                heappush(q, (cost, next))
    return dist[end]

N, E = map(int, input().split())
# 그래프 초기화
graph = {i: [] for i in range(1, N+1)}

# 간선 초기화
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())
v1tov2 = dijkstra(v1, v2)
result = min(dijkstra(1, v1) + v1tov2 + dijkstra(v2, N), dijkstra(1, v2) + v1tov2 + dijkstra(v1, N))
print(result if result < INF else -1)