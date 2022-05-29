import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra(start, end):
    q = [(0, start)]
    dist = [INF] * (V + 1)
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

V, E, P = map(int, input().split())
# 그래프 초기화
graph = {i: [] for i in range(1, V+1)}

# 간선 초기화
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print("SAVE HIM" if dijkstra(1, V) == dijkstra(1, P) + dijkstra(P, V) else "GOOD BYE")