from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dist = [[[0] * M for _ in range(N)] for _ in range(2)]
answer = -1

q = deque([(1, 0, 0)])
dist[1][0][0] = 1

while q:
    cnt, x, y = q.popleft()

    if x == N-1 and y == M-1:
        answer = dist[cnt][x][y]
        break

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and not dist[cnt][nx][ny]:
            if cnt == 1 and board[nx][ny] == "1":
                dist[cnt-1][nx][ny] = dist[cnt][x][y] + 1
                q.append((cnt-1, nx, ny))
            if board[nx][ny] == "0":
                dist[cnt][nx][ny] = dist[cnt][x][y] + 1
                q.append((cnt, nx, ny))
print(answer)