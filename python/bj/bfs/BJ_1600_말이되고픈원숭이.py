from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

K = int(input())
M, N = map(int, input().split())
board = [input().split() for _ in range(N)]

dist = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
dist[0][0][0] = 0

q = deque([(0, 0, 0)])

while q:
    level, x, y = q.popleft()
    
    if x == N - 1 and y == M - 1:
        print(dist[level][x][y])
        sys.exit()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '1' and dist[level][nx][ny] == -1:
            dist[level][nx][ny] = dist[level][x][y] + 1
            q.append((level, nx, ny))

    for nx, ny in [(x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2), (x-2, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '1' and level + 1 <= K and dist[level+1][nx][ny] == -1:
            dist[level+1][nx][ny] = dist[level][x][y] + 1
            q.append((level + 1, nx, ny))
print(-1)