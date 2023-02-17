from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
j_q, f_q = deque(), deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == "J":
            j_q.append((i, j))
        elif board[i][j] == "F":
            f_q.append((i, j))
            dist[i][j] = 0

while f_q:
    x, y = f_q.popleft()
    for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != "#" and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            f_q.append((nx, ny))

l = 0
while j_q:
    for _ in range(len(j_q)):
        x, y = j_q.popleft()

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] not in "#J" and (dist[nx][ny] == -1 or l <= dist[nx][ny]):
                    board[nx][ny] = "J"
                    j_q.append((nx, ny))
            else:
                print(l+1)
                exit()
    l += 1
print("IMPOSSIBLE")