import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def dijkstra(start, end, have_coin):
    q = [(0, start, have_coin)]
    dist = [INF] * (N + 1)
    dist[start] = 0
    
    while q:
        cur_cost, cur_node, cur_coin = heappop(q)
        
        if dist[cur_node] < cur_cost:
            continue
        
        for next_node, next_cost in graph[cur_node]:
            next_have_coin = cur_coin - next_cost
            max_cost = max(cur_cost, next_cost)
            if next_have_coin >= 0 and dist[next_node] > max_cost:
                dist[next_node] =max_cost
                heappush(q, (max_cost, next_node, next_have_coin))
                
    return -1 if dist[end] == INF else dist[end]
    
INF = sys.maxsize
N, M, A, B, C = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(dijkstra(A, B, C))