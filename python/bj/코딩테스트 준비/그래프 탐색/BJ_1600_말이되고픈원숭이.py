from collections import deque

K = int(input())
M, N = map(int, input().split())
board = [input().split() for _ in range(N)]
dist = [[[-1] * M for _ in range(N)] for _ in range(K+1)]

q = deque([(K, 0, 0)])
dist[K][0][0] = 0
while q:
    cnt, x, y = q.popleft()

    if x == N-1 and y == M-1:
        print(dist[cnt][x][y])
        exit()

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and dist[cnt][nx][ny] == -1 and board[nx][ny] != "1":
            dist[cnt][nx][ny] = dist[cnt][x][y] + 1
            q.append((cnt, nx, ny))

    if cnt > 0:
        for nx, ny in [(x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2), (x-2, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and dist[cnt-1][nx][ny] == -1 and board[nx][ny] != "1":
                dist[cnt-1][nx][ny] = dist[cnt][x][y] + 1
                q.append((cnt-1, nx, ny))
print(-1)