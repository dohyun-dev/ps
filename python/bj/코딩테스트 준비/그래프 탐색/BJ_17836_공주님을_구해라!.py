from collections import deque

N, M, T = map(int, input().split())
board = [input().split() for _ in range(N)]
dist = [[[0] * M for _ in range(N)] for _ in range(2)]

q = deque([(0, 0, 0)])
while q:
    x, y, c = q.popleft()

    if x == N-1 and y == M-1 and dist[c][x][y] <= T:
        print(dist[c][x][y])
        exit()

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == "0":
                if dist[c][nx][ny]:
                    continue
                dist[c][nx][ny] = dist[c][x][y] + 1
                q.append((nx, ny, c))
            elif board[nx][ny] == "1":
                if c != 1:
                    continue
                dist[c][nx][ny] = dist[c][x][y] + 1
                q.append((nx, ny, c))
            else:
                dist[c+1][nx][ny] = dist[c][x][y] + 1
                q.append((nx, ny, c+1))
            board[nx][ny] = "0"
print("Fail")