def make_board(m, n, puddles):
    board = [[0] * m for _ in range(n)]
    board[0][0] = 1
    return board

def solution(m, n, puddles):
    board = make_board(m, n, puddles)
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                board[i][j] = 0
            else:
                board[i][j] += (board[i-1][j] + board[i][j-1]) % 1000000007
    return board[n-1][m-1]

print(solution(4, 3, [[2, 2]]))