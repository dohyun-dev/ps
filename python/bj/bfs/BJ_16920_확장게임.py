import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M, P = map(int, input().split())
s = [0] + list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
result = [0] * (P + 1)

castles = [deque() for _ in range(P+1)]

for i in range(N):
    for j in range(M):
        if board[i][j] not in '.#':
            castle = int(board[i][j])
            board[i][j] = castle
            result[castle] += 1
            castles[castle].append((i, j))

while True:
    flag = True
    for i in range(1, P+1):
        if castles[i]:
            q = castles[i]
            for _ in range(s[i]):
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == ".":
                            board[nx][ny] = i
                            q.append((nx, ny))
                            result[i] += 1
            castles[i] = q
            flag = False
    if flag:
        break
print(*result[1:])
