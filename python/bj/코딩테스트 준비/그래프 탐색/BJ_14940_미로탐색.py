from collections import deque

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
dist = [[0] * M for _ in range(N)]
for i in range(N):
    flag = False
    for j in range(M):
        if board[i][j] == "2":
            flag = True
            q = deque([(i, j)])
            board[i][j] = "0"

            while q:
                x, y = q.popleft()

                for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1":
                        board[nx][ny] = "0"
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
            break
    if flag:
        break

print("\n".join(
    " ".join(
        "-1" if board[i][j] == "1" and dist[i][j] == 0
        else str(dist[i][j])
        for j in range(M))
    for i in range(N)))