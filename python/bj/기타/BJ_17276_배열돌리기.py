import sys; input = lambda : sys.stdin.readline().rstrip()
from copy import deepcopy

def turn(board, angle, n):
        for _ in range(abs(angle) // 45):
            new_board = deepcopy(board)
            if angle > 0:
                # 1
                for i in range(N):
                    new_board[i][n//2] = board[i][i]
                # 2
                for i in range(N):
                    new_board[i][n-i-1] = board[i][n//2]
                #3
                for i in range(N):
                    new_board[n//2][n-i-1] = board[i][n-i-1]
                #4
                for i in range(N):    
                    new_board[i][i] = board[n//2][i]
            elif angle < 0:
                # 1
                for i in range(N):
                    new_board[n//2][i] = board[i][i]
                # 2
                for i in range(N):
                    new_board[n-i-1][i] = board[n//2][i]
                #3
                for i in range(N):
                    new_board[i][n//2] = board[i][n-i-1]
                #4
                for i in range(N):    
                    new_board[i][i] = board[i][n//2]
            board = new_board
        return board

for _ in range(int(input())):
    N, angle = map(int, input().split())
    board = [input().split() for _ in range(N)]
    board = turn(board, angle, N)
    print("\n".join([" ".join(b) for b in board]))    