import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict
sys.setrecursionlimit(200000)

def DFS(node, nodes, graph):
    result = 0
    
    for next in graph[node]:
        result += DFS(next, nodes, graph)
        
    if nodes[node][0] == "S":
        result += nodes[node][1]
    elif nodes[node][0] == "W":
        result -= nodes[node][1]
    if result <= 0:
        result = 0
    return result

N = int(input())
graph = defaultdict(list)
nodes = [(0, 0) for _ in range(N+1)]
result = 0

for i in range(2, N+1):
    temp = input().split()
    a = temp[0] 
    b, c = map(int, temp[1:])
    graph[c].append(i)
    nodes[i] = (a, b)

print(DFS(1, nodes, graph))