from collections import deque;
import sys; input = lambda : sys.stdin.readline().rstrip()

def spread(board):
    q = deque([(i, j) for j in range(M) for i in range(N) if board[i][j] == 2])
    x, y = q[0]
    board[x][y] = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
    return sum([1 for j in range(M) for i in range(N) if board[i][j] == 0])

def wall(l, r, c):
    global answer
    if l == 3:
        answer = max(answer, spread([b[:] for b in board]))
        return
    else:
        for i in range(r, N):
            if r == i:
                c1 = c
            else:
                c1 = 0
            for j in range(c1, M):
                if board[i][j] == 0:
                    board[i][j] = 1
                    wall(l+1, i, j+1)
                    board[i][j] = 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
wall(0, 0, 0)
print(answer)