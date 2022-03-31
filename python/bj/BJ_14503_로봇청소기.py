import sys
input = lambda : sys.stdin.readline().rstrip()


dir = [(-1, 0), (0, 1), (1, 0), (0,-1)] # 북 동 남 서
answer = 0

N, M = map(int, input().split())
a, b, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def clean(x, y, d):
    global answer
    
    if board[x][y] == 0:
        board[x][y] = -1
        answer += 1
    
    for i in range(4):
        cur_d = abs(d - i + 3) % 4
        nx, ny = dir[cur_d][0] + x, dir[cur_d][1] + y
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            clean(nx, ny, cur_d)
            break
        cur_d -= 1
    else:
        nx, ny = dir[(cur_d + 2) % 4][0] + x, dir[(cur_d + 2) % 4][1] + y
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == -1:
            clean(nx, ny, d)

clean(a, b, c)            
print(answer)