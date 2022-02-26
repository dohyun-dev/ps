import sys; input = lambda : sys.stdin.readline().rstrip()

def up(board):
    for i in range(N):
        p = 0 
        x = 0
        for j in range(N):
            if board[j][i] == 0: continue
            if x == 0: x = board[j][i]
            else:
                if x == board[j][i]:
                    board[p][i] = x * 2
                    x = 0
                    p += 1
                else:
                    board[p][i] = x
                    x = board[j][i]
                    p += 1
            board[j][i] = 0 
        if x != 0: board[p][i] = x 
        

def down(board):
    for j in range(N):
        for i in range(N-2, -1, -1):
            if board[j][i] == 0:   
                board[j][i] = board[j+1][i]
                board[j+1][i] = 0
            if board[j][i] == board[j+1][i]:
                board[j][i] = board[j][i] * 2
                board[j+1][i] = 0

def left(board):
    for i in range(N):
        for j in range(N-2, -1, -1):
            if board[i][j] == 0:   
                board[i][j] = board[i][j+1]
                board[i][j+1] = 0
            if board[i][j] == board[i][j+1]:
                board[i][j] = board[i][j] * 2
                board[i][j+1] = 0

def right(board):
    for i in range(N):
        for j in range(1, N):
            if board[i][j] == 0:   
                board[i][j] = board[i][j-1]
                board[i][j-1] = 0
            if board[i][j] == board[i][j-1]:
                board[i][j] = board[i][j] * 2
                board[i][j-1] = 0
                
                
def solve(direction, board):
    for d in direction:
        if d == "U":
            up(board)
        elif d == "D":
            down(board)
        elif d == "L":
            left(board)
        else:
            right(board)
    result = -sys.maxsize
    
    for i in range(N):
        for j in range(N):
            result = max(result, board[i][j])
    
    return result
    
    

dir = ["U", "D", "L", "R"]
result = []
max_value = -sys.maxsize
def combinations(board, l = 0):
    global max_value
    if l == 5:
        temp = [board[i][:] for i in range(N)]
        max_value = max(max_value, solve(result, temp))
        return
    for i in range(4):
        result.append()
        combinations(board, l+1, i)
        result.pop()

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
left(board)
print("\n".join(map(str, board)))
