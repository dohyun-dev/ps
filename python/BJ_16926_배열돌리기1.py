import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
board = [input().split() for _ in range(N)]
group = min(N, M) // 2

for _ in range(R):
    for i in range(group):
        temp = board[i][i]
        
        for j in range(i, M-i-1):   board[i][j] = board[i][j+1]
        for j in range(i, N-i-1):   board[j][M-i-1] = board[j+1][M-i-1]
        for j in range(M-i-1, i, -1):    board[N-i-1][j] = board[N-i-1][j-1]
        for j in range(N-i-1, i, -1):    board[j][i] = board[j-1][i]
        board[i+1][i] = temp


for b in board:
    for i in b:
        print(i, end=" ")
    print()