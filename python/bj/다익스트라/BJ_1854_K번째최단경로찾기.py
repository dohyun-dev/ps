import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

def dijkstra():
    q = [(0, 1)]
    dist = [[INF] * K for _ in range(N+1)]
    dist[1][0] = 0
    
    while q:
        cur_dist, cur_node = heappop(q)
        
        for next_node, next_cost in graph[cur_node]:
            next_dist = cur_dist + next_cost
            if dist[next_node][K-1] > next_dist:
                dist[next_node][K-1] = next_dist
                dist[next_node].sort()
                heappush(q, (next_dist, next_node))
    return map(lambda x: "-1" if x[K-1] == INF else str(x[K-1]), dist[1:])
    
N, M, K = map(int, input().split())
graph = {i : [] for i in range(1, N+1)}
INF = sys.maxsize

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print("\n".join(dijkstra()))