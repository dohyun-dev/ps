import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(r, c, cnt = 0):
    global answer
    if check(board) and cnt < answer:
        answer = cnt
        if cnt == 0:
            print(answer)
            sys.exit()
        return
    if cnt == 3 or r == H+2:
        return
    else:
        for i in range(r, H+1):
            if r == i:  c2 = c
            else:       c2 = 1
            for j in range(c2, N):
                if board[i][j] == 1:
                    continue
                if board[i][j-1] == 1:
                    continue
                if board[i][j+1] == 1:
                    continue
                board[i][j] = 1
                DFS(i, j, cnt+1)
                board[i][j] = 0
                    
def check(board):
    for c in range(1, N+1):
        cur_col = c
        for r in range(H, -1, -1):
            if board[r][cur_col-1] == 1:
                cur_col -= 1
                continue
            elif cur_col + 1 <= N and board[r][cur_col] == 1:
                cur_col += 1
                continue
        if cur_col != c:
            return False
    else:
        return True

N, M, H = map(int, input().split())
board = [[0] * (N + 1) for _ in range(H + 1)]
answer = sys.maxsize

for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

DFS(1, 1)
print(-1 if answer == sys.maxsize else answer)