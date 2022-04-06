from collections import deque
import sys; input =lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dist = [[[-1] * M for i in range(N)] for _ in range(2)]

q = deque([(0, 0 ,0)])
dist[0][0][0] = 0

while q:
    c, x, y = q.popleft()
    
    if x == N - 1 and y == M - 1:
        print(dist[c][x][y] + 1)
        sys.exit()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '1' and c < 1 and dist[c+1][nx][ny] == -1:
                dist[c+1][nx][ny] = dist[c][x][y] + 1
                q.append((c+1, nx, ny))
            if board[nx][ny] == '0' and dist[c][nx][ny] == -1:
                dist[c][nx][ny] = dist[c][x][y] + 1
                q.append((c, nx, ny))
print(-1)