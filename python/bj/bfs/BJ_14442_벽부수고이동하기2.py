from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
dist = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
dist[0][0][0] = 1

q = deque([(0, 0, 0)])

while q:
    level, x, y = q.popleft()
    
    if x == N-1 and y == M-1:
        print(dist[level][x][y])
        sys.exit()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == '1':
                if level + 1 <= K and dist[level+1][nx][ny] == -1:
                    dist[level+1][nx][ny] = dist[level][x][y] + 1
                    q.append((level+1, nx, ny))
            else:
                if dist[level][nx][ny] == -1:
                    dist[level][nx][ny] = dist[level][x][y] + 1
                    q.append((level, nx, ny))
print(-1)