import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def dijkstra(start, end):
    q = [(start, 1)]
    dist = [[INF] * 2 for _ in range(N+1)]
    dist[start][0] = 0
    
    while q:
        cur_dist, cur_node = heappop(q)
        
        for next_node, next_cost in graph[cur_node]:
            next_dist = cur_dist + next_cost
            if dist[next_node][1] > next_dist:
                dist[next_node][1] = next_dist
                dist[next_node].sort()
                heappush(q, (next_dist, next_node))
    return -1 if dist[end][1] == INF else dist[end][1]

result = []
while True:    
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    S, D = map(int, input().split())
    graph = {i : [] for i in range(N+1)}
    INF = sys.maxsize

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    result.append(dijkstra(S, D))
print("\n".join(map(str, result)))