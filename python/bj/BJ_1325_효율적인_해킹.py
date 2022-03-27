import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

result = [(0, 0)]   # 노드 번호 해킹한 컴퓨터 수

def BFS(a, graph, N):
    q = deque([a])
    visited = [False] * (N + 1)
    visited[a] = True
    cnt = 1
    while q:
        for _ in range(len(q)):
            cur = q.popleft()
            for next in graph[cur]:
                if not visited[next]:
                    visited[next] = True
                    q.append(next)
                    cnt+=1
    if result[0][1] < cnt:
        result.clear()
        result.append((a, cnt))
    elif result[0][1] == cnt:
        result.append((a, cnt))

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)
    
    for i in range(1, N+1):
        BFS(i, graph, N)
    
    print(" ".join(map(lambda x : str(x[0]), sorted(result, key=lambda x : x[0]))))