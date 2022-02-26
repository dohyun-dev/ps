from collections import deque

def BFS(start, visited, graph):
    q = deque([start])
    visited[start] = True
    result = []
    while q:
        temp = []
        for _ in range(len(q)):
            cur = q.popleft()
            temp.append(cur)
            for next in graph[cur]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
        result.append(temp)
    return sorted(result[-1], reverse=True)[0]


result = []
for t in range(1, 11):
    
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    temp = list(map(int, input().split()))
    visited = {}
    for i in range(0, n, 2):
        a, b = temp[i], temp[i+1]
        graph[a].append(b)
    
    for i in temp:
        visited[i] = False;
        
    result.append(f'#{t} {BFS(start, visited, graph)}')
print("\n".join(map(str, result)))
        
    