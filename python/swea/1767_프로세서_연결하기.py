k = 0
arr = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y, dir, board):
    nx, ny = x, y
    while True:
        nx = nx + dx[dir]
        ny = ny + dy[dir]
        if not(0 <= nx < N and 0 <= ny < N):
            break
        if board[nx][ny] in (1, 2):
            return False
        board[nx][ny] = 2
    return True

def solve(board, l=0):
    global answer
    if l == 0:
        board = [b[:] for b in board]
    if l == k:
        tmp = sum([b.count(2) for b in board])
        if tmp < answer:
            answer = tmp
        return
    else:
        for i in range(4):
            if check(cores[l][0], cores[l][1], i, board):
                arr.append(i)
                solve(board, l+1)
                arr.pop()

result = []
for t in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = float("inf")
    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j]: cores.append((i, j))
    k = len(cores)
    
    solve(board)
    
    result.append(f'#{t} {answer}')
print("\n".join(result))