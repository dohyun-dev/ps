from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def count_cheese(board):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt

def bfs1(x, y, board):
    q = deque([(x, y)])
    board[x][y] = 2
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                
def get_remove_cheese_list(q, board):
    erase_list = []
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 2:
                erase_list.append((x, y))
                break
    return erase_list

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
hour, answer = 0, count_cheese(board)
while True:
    hour += 1
    board_temp = [b[:] for b in board]
    bfs1(0, 0, board_temp)
    
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                q.append((i, j))
    
    for x, y in get_remove_cheese_list(q, board_temp):
        board[x][y] = 0
    
    cnt = count_cheese(board)
    if cnt == 0:
        break
    answer = cnt
print(hour, answer, sep="\n")