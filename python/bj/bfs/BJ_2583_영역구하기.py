from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def bfs(x, y, board):
    q = deque([(x, y)])
    board[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                cnt += 1
                board[nx][ny] = 1
                q.append((nx, ny))
    return str(cnt)

N, M, f = map(int, input().split())
board = [[0] * M for _ in range(N)]
answer = []
for _ in range(f):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            answer.append(bfs(i, j, board))
print(len(answer))
print(" ".join(sorted(answer, key=lambda x: int(x))))