from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
answer = 0

q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))
        elif board[i][j] == -1:
            dist[i][j] = -2

while q:
    x, y = q.popleft()
    
    if dist[x][y] > answer:
        answer = dist[x][y]

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
print(-1 if any([any(map(lambda x : x == -1, d)) for d in dist]) else answer)