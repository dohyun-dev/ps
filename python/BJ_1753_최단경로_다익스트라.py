import sys; input = lambda : sys.stdin.readline().rstrip();
from collections import defaultdict
import heapq

def dijkstra(start):
    dist = [sys.maxsize] * (N + 1)
    dist[start] = 0
    q = []; heapq.heappush(q, (0, start))
    
    while q:
        cost, cur = heapq.heappop(q)
        
        if dist[cur] < cost:
            continue
        for next, next_cost in graph[cur]:
            if dist[next] > cost + next_cost:
                dist[next] = cost + next_cost
                heapq.heappush(q, (dist[next], next))
    
    return dist[1:]

N, M = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

print("\n".join(map(lambda x: str(x) if x != sys.maxsize else "INF", dijkstra(start))))