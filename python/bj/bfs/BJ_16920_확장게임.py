import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque;  sys.setrecursionlimit(100000)

def DFS(x, y, cur, limit, q, visited, cnt=0):
    visited[x][y] = True
    if cnt == limit:
        return
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '.':
                q.append((cur, nx, ny))
                board[nx][ny] = str(cur)
                result[cur] += 1
                DFS(nx, ny, cur, limit, q, visited, cnt+1)
            elif board[nx][ny] == str(cur) and not visited[nx][ny]:
                DFS(nx, ny, cur, limit, q, visited, cnt+1)
    
N, M, P = map(int, input().split())
s = [0] + list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
result = [0] * (P + 1)

q = []
for i in range(N):
    for j in range(M):
        if board[i][j] not in '.#':
            result[int(board[i][j])] += 1
            q.append((int(board[i][j]), i, j))
q = deque(sorted(q, key=lambda x: x[0]))

while q:
    cur, x, y = q.popleft()
    visited = [[False] * M for _ in range(N)]
    DFS(x, y, cur, s[cur], q, visited)

print(' '.join(str(x) for x in result[1:]))