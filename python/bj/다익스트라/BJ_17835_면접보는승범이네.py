import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

INF = sys.maxsize
def dijkstra():
    q = []
    dist = [INF] * (N + 1)
    for meeting in meetings:
        heappush(q, (0, meeting))
        dist[meeting] = 0
    
    while q:
        cur_cost, cur = heappop(q)
        
        if dist[cur] < cur_cost:    
            continue
        
        for next, next_cost in graph[cur]:
            cost = cur_cost + next_cost
            if cost < dist[next]:
                dist[next] = cost
                heappush(q, (cost, next))
    
    max_i, max_dist = 0, 0
    for i in range(1, N+1):
        if max_dist < dist[i]:
            max_i, max_dist = i, dist[i]
    return list(map(str, (max_i, max_dist)))

N, M, K = map(int, input().split())
# 그래프 초기화
graph = {i: [] for i in range(1, N+1)}

# 간선 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
meetings = list(map(int, input().split()))

print("\n".join(dijkstra()))