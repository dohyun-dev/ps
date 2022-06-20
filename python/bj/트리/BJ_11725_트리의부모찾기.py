import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict, deque

def bfs(cur):
    q = deque([cur])
    visited = [False] * (N + 1)
    visited[cur] = True

    while q:
        cur = q.popleft()
        for next in tree[cur]:
            if parent[next] == 0:
                parent[next] = cur
                q.append(next)

    return "\n".join(map(str, parent[2:]))

N = int(input())
tree = defaultdict(list)
parent = [0] * (N + 1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(bfs(1))
