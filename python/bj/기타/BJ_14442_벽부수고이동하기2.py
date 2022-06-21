from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
board = [list(map(int, *input().split())) for _ in range(N)]
dist = [[[-1] * M for i in range(N)] for _ in range(K+1)]
q = deque([(0, 0, 0)])
dist[0][0][0] = 1

while q:
    c, x, y = q.popleft()
    
    if x == N-1 and y == M-1:
        print(dist[c][x][y])
        sys.exit()
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                if dist[c][nx][ny] == -1 :
                    dist[c][nx][ny] = dist[c][x][y] + 1
                    q.append((c, nx, ny))
            else:
                if c + 1 <= K and dist[c+1][nx][ny] == -1:
                    dist[c+1][nx][ny] = dist[c][x][y] + 1
                    q.append((c+1, nx, ny))
print(-1)