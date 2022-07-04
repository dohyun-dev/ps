import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def BFS():
    q = deque([1])
    visited = [False] * (N+M+1)
    visited[1] = True
    level = 0

    while q:
        if q:
            if q[0] <= N:
                level += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur == N:
                return level
            for next_node in graph[cur]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
    return -1

N, K, M = map(int, input().split())
graph = {i: [] for i in range(1, N+M+1)}

for i in range(N+1, N+M+1):
    graph[i] = [*map(int, input().split())]
    for j in graph[i]:
        graph[j].append(i)
print(BFS())