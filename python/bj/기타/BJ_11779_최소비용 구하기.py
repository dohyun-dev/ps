import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque; import heapq

def dijkstra(start, end):
    dist = [sys.maxsize] * (N + 1); dist[start] = 0
    q = []; heapq.heappush(q, (0, start))
    path = defaultdict(list);  path[start].append(start)
    
    while q:
        cost, cur = heapq.heappop(q)
        
        if dist[cur] < cost:
            continue
        for next, next_cost in graph[cur]:
            if next_cost + cost < dist[next]:
                dist[next] = next_cost + cost
                heapq.heappush(q, (dist[next], next))
                path[next] = path[cur] + [next]
                
    return path[end], dist[end]

N, M = int(input()), int(input())
graph = defaultdict(list)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())
result, result_cost = dijkstra(start, end)
print(result_cost, len(result), " ".join(map(str, result)), sep="\n")