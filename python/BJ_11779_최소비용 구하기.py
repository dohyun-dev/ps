# import sys; input = lambda : sys.stdin.readline().rstrip()
# from collections import defaultdict, deque; import heapq

# def dijkstra(start, end):
#     q = []
#     dist = [sys.maxsize] * (N + 1)
#     dist[start] = 0
#     path = [-1 for _ in range(N + 1)]
#     heapq.heappush(q, (0, start))
    
#     while q:
#         cur_cost, cur = heapq.heappop(q)
        
#         if cur == end:
#             print(dist[cur])
#             result = deque([end])
#             while end != start:
#                 result.appendleft(path[end])
#                 end = path[end]
            
#             print(len(result))
#             print(*result)
        
#         for next, nest_cost in graph[cur]:
#             temp = cur_cost + nest_cost
#             if dist[next] > temp:
#                 dist[next] = temp
#                 heapq.heappush(q, (temp, next))
#                 path[next] = cur

# N, M = int(input()), int(input())
# graph = defaultdict(list)

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))
    
# start, end = map(int, input().split())
# dijkstra(start, end)
import heapq
n = int(input())
m = int(input())
 
graph = [[] for _ in range(n + 1)]
INF = int(1e9)
dist = [INF] * (n + 1)
parent = [i for i in range(n + 1)]
 
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
 
start, end = map(int, input().split())
 
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
 
    while q:
        distance, now = heapq.heappop(q)
        if dist[now] < distance:
            continue
        for i in graph[now]:
            cost = distance + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                parent[i[0]] = now
        
dijkstra(start)
print(dist[end])
st = []
cnt = 1
i = end
st.append(i)
while i != start:
    i = parent[i]
    cnt += 1
    st.append(i)
 
print(cnt)
while st:
    print(st.pop(), end=' ')