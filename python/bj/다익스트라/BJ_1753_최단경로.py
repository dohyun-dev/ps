import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra(start):
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
    return "\n".join(str(dist[i]) if dist[i] != INF else "INF" for i in range(1, V+1))

V, E = map(int, input().split())
start = int(input())

# 그래프 초기화
graph = {i: [] for i in range(1, V+1)}

# 간선 초기화
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
print(dijkstra(start))