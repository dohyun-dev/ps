temp = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean_up_board(x, y, board):
    for i in range(W):
        bot = x
        top = x - 1
        while top >= 0:
            if board[bot][i] == 0:
                if board[top][i] != 0:
                    board[bot][i] = board[top][i]
                    board[top][i] = 0
                    bot, top = bot - 1, top - 1
                else:
                    top -= 1


def break_process(break_list, board):
    total = 0
    for x, y, cnt in break_list:
        
        nx, ny = x, y
        while cnt:
            for i in range(4):
                nx, ny = nx + dx[i], ny + dy[i]
                if not(0 <= nx < H and 0 <= ny < W):
                    break
                if board[nx][ny] == 1:
                    board[nx][ny] = 0  
                    total += 1       
                cnt -= 1
    return total



def break_list_process(x, y, power, board):
    cnt = 0
    break_list = [(x, y, 1)]
    for i in range(4):
        nx = x * (dx[i] * power)
        ny = y * (dy[i] * power)
        if 0 <= nx < H and 0 <= ny < W:
            board[nx][ny] = 0
            break_list.append((nx, ny, board[nx][ny]))
    
    cnt += break_process(break_list, board)
    

def process(board):
    total = 0
    for c in temp:
        for i in range(H):
            if board[c][i] != 0:
                board[c][i] = 0
                total += break_list_process(i, c, 1, board)
                break
    return total

def dfs(l=0):
    global answer
    if l == N:
        answer = max(answer, process([b[:] for b in board]))
        return
    for i in range(W):
        temp.append(i)
        dfs(l+1)
        temp.pop()

for t in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    answer = 0
    dfs()
    print(f'{t} {answer}')