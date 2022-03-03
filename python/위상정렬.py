import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

graph = {}
graph[0] = [1]
graph[1] = []
graph[2] = [1, 3]
graph[3] = [1, 4]
graph[4] = [5]
graph[5] = []
graph[6] = [4]

indegree = [0] * 7

for key, value in graph.items():
    for i in value:
        indegree[i] += 1

q = deque([i for i in range(7) if indegree[i] == 0])
result = []
while q:
    cur = q.popleft()
    result.append(cur)

    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)

for i in result:
    print(chr(65 + i))