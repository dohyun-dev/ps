from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
j_q, f_q = deque(), deque()
dist = [[-1] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 'J':
            j_q.append((i, j))
        elif board[i][j] == 'F':
            f_q.append((i, j))
            dist[i][j] = 0

while f_q:
    x, y = f_q.popleft()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            f_q.append((nx, ny))

level = 0
while j_q:
    for _ in range(len(j_q)):
        x, y = j_q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != '#' and (dist[nx][ny] == -1 or level + 1 < dist[nx][ny]):
                    board[nx][ny] = '#'
                    j_q.append((nx, ny))
            else:
                print(level + 1)
                sys.exit()
    level += 1
print("IMPOSSIBLE")