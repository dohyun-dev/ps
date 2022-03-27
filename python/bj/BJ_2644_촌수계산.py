import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque

n = int(input())
node1, node2 = map(int, input().split())
graph = defaultdict(list)

for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque([node1])
visited = [False] * (n + 1)
visited[node1] = True
res = 0
while q:
    for _ in range(len(q)):
        cur = q.popleft()
        for next in graph[cur]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                if next == node2:
                    print(res + 1)
                    sys.exit()
    res += 1
print(-1)