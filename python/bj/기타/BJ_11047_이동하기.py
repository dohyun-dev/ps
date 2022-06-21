N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, M):   board[0][i] += board[0][i-1]
for i in range(1, N):   board[i][0] += board[i-1][0]

for i in range(1, N):
    for j in range(1, M):
        board[i][j] = max(board[i-1][j-1], board[i-1][j], board[i][j-1]) + board[i][j]
print(board[N-1][M-1])