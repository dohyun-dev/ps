from collections import deque

R, C, N = map(int, input().split())
board = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == "O":
            board[i][j] = 3

for i in range(2, N+1):
    if i % 2 == 0:
        for r in range(R):
            for c in range(C):
                if board[r][c] == ".":
                    board[r][c] = i + 3
    else:
        q = deque((x, y) for y in range(C) for x in range(R) if board[x][y] == i)
        while q:
            x, y = q.popleft()
            for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0 <= nx < R and 0 <= ny < C:
                    board[nx][ny] = "."
            board[x][y] = "."
print("\n".join("".join(map(lambda x: x if x == "." else "O", b)) for b in board))

