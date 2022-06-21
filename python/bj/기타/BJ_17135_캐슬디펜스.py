from itertools import combinations
from heapq import heappush, heappop
import sys; input = lambda : sys.stdin.readline().rstrip()

def search(board):
    candidate_list = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                candidate_list.append((i, j))
    return candidate_list

def fall(board, level):
    for i in range(M):
        for j in range(N-1, 0, -1):
            board[j][i] = board[j-1][i]
    for i in range(M):
        board[level][i] = 0

def atack(x, y, board, candidate_list):
    atack_list = []
    for t_x, t_y in candidate_list:
        dist = abs(t_x - x) + abs(t_y - y)
        if dist <= D:
            heappush(atack_list, (dist, t_y, t_x))
            
    if atack_list:
        dist, y, x = heappop(atack_list)
        if board[x][y] == 1:
            board[x][y] = 0
            return 1
        else:
            return 0
    else:
        return 0

def check(board):
    cnt = 0
    for i in range(N-1, -1, -1):  
        for j in range(M):
           if board[i][j] == 1:
               return True
    return False

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
answer = 0

for y_list in combinations([i for i in range(M)], 3):
    cnt = 0
    temp = [b[:] for b in board]
    level = 0
    while check(temp):
        candidate_list = search(temp)
        for y in y_list:
            cnt += atack(N, y, temp, candidate_list)
        fall(temp, level)
        level += 1
    answer = max(answer, cnt)
print(answer)