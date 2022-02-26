import sys; input = lambda : sys.stdin.readline().rstrip();
from collections import defaultdict
import heapq

def dijkstra(start):
    dist = [sys.maxsize for i in range(N+1)]
    q = []
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))
    
    while q:
        cur_distance, cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_distance:   continue
        for next_node, next_distance in graph[cur_node]:
            if dist[next_node] > cur_distance + next_distance:
                dist[next_node] = cur_distance + next_distance
                heapq.heappush(q, (dist[next_node], next_node))
    return dist

N, M = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))
    
print("\n".join(map(lambda x: "INF" if x == sys.maxsize else str(x), dijkstra(start)[1:])))
