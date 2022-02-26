import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque
from heapq import *

def BFS(x, y, board, N, cur_size):
    eat_list = []
    q = deque([(x, y)])
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    
    cnt = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
                    visited[dx][dy] = True
                    if board[dx][dy] <= cur_size:
                        q.append((dx, dy))
                    if board[dx][dy] != 0 and board[dx][dy] < cur_size:
                        eat_list.append((dx, dy, cnt+1))
        cnt += 1
    eat_list.sort(key=lambda x : (x[2], x[0], x[1]))
    return eat_list;

def eat(eat_thing):
    global cur_x, cur_y, level_up_cnt, cur_size
    level_up_cnt += 1
    if level_up_cnt == cur_size:
        cur_size += 1
        level_up_cnt = 0
    x, y, cnt = eat_thing
    board[cur_x][cur_y] = 0
    board[x][y] = 9
    cur_x, cur_y = x, y
    return cnt

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cur_size = 2
level_up_cnt = 0
time = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            cur_x, cur_y = i, j
            break
while True:
    eat_list = BFS(cur_x, cur_y, board, N, cur_size)
    if not eat_list:
        break
    time += eat(eat_list[0])
print(time)