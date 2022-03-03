from distutils.log import fatal
import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, graph, M = int(input()), {name:[] for name in input().split()}, int(input())
indegree = {name:0 for name in graph.keys()}

for _ in range(M):
    a, b = input().split()
    graph[b].append(a)
    indegree[a] += 1

q = deque()    
root = []
child = {name:[] for name in graph.keys()}

for cur in graph.keys():
    if indegree[cur] == 0:
        q.append(cur)
        root.append(cur)

while q:
    cur = q.popleft()
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] == 0:
            q.append(node)
            child[cur].append(node)

print(str(len(root)) + "\n" + " ".join(sorted(root)))
for cur in sorted(graph.keys()):
    print(cur, str(len(child[cur])), end = " ")
    print(" ".join(sorted(child[cur])))
