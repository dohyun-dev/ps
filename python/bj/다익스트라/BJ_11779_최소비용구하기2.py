import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra(start, end):
    q = [(0, start)]
    path = [[] for _ in range(N+1)]
    dist = [INF] * (N + 1)
    dist[start], path[start] = 0, [start]
    
    while q:
        cur_cost, cur = heappop(q)
        
        if dist[cur] < cur_cost:    
            continue
        
        for next, next_cost in graph[cur]:
            cost = cur_cost + next_cost
            if cost < dist[next]:
                dist[next] = cost
                path[next] = path[cur] + [next]
                heappush(q, (cost, next))
    return (dist[end], path[end])

N, M = int(input()), int(input())
# 그래프 초기화
graph = {i: [] for i in range(1, N+1)}

# 간선 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
start, end = map(int, input().split())
dist, path = dijkstra(start, end)
print(dist, len(path), " ".join(map(str, path)), sep="\n")