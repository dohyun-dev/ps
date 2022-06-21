import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
board = [input().split() for _ in range(N)]
g = min(N, M) // 2

for _ in range(R):
    for i in range(g):
        temp = board[i][i]
        for j in range(i, M-i-1):       
            board[i][j] = board[i][j+1]
        for j in range(i, N-i-1):       
            board[j][M-i-1] = board[j+1][M-i-1]
        for j in range(M-i-1, i, -1):     
            board[N-i-1][j] = board[N-i-1][j-1]
        for j in range(N-i-1, i, -1):     
            board[j][i] = board[j-1][i]
        board[i+1][i] = temp

print("\n".join([" ".join(b) for b in board]))