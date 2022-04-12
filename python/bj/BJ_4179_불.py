from collections import deque


def f_bfs(q, board, f_dist):
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and f_dist[nx][ny] == -1:
                f_dist[nx][ny] = f_dist[x][y] + 1
                q.append((nx, ny))

def j_bfs(q, board, j_dist, f_dist):
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if not (0 <= nx < N and 0 <= ny < M):
                return j_dist[x][y] + 1
            elif board[nx][ny] != '#' and j_dist[nx][ny] == -1:
                if f_dist[nx][ny] == -1 or j_dist[x][y] + 1 < f_dist[nx][ny]:
                    j_dist[nx][ny] = j_dist[x][y] + 1
                    q.append((nx, ny))
    return "IMPOSSIBLE"

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

j_q, f_q = deque(), deque()
j_dist = [[-1] * M for _ in range(N)]
f_dist = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'J':
            j_dist[i][j] = 0
            j_q.append((i, j))
        elif board[i][j] == 'F':
            f_dist[i][j] = 0
            f_q.append((i, j))

f_bfs(f_q, board, f_dist)
print(j_bfs(j_q, board, j_dist, f_dist))