from collections import deque
from enum import Flag
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board):
    q = deque([(x, y)])
    find_char = board[x][y]
    visited = [[False] * 6 for _ in range(12)]
    visited[x][y] = True
    update_list = [(x, y)]
    
    while q:
        x, y = q.popleft()
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < 12 and 0 <= ny < 6:
                if not visited[nx][ny] and board[nx][ny] == find_char:
                    update_list.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    if len(update_list) >= 4:
        for x, y in update_list:
            board[x][y] = "."
        return 1
    return 0

def gravity(board):
    for i in range(6):
        q = deque()
        
        for j in range(11, -1, -1):
            if board[j][i] != ".":
                q.append(board[j][i])
        
        for j in range(11, -1, -1):
            if q:
                board[j][i] = q.popleft()
            else:
                board[j][i] = "."


board = [list(*input().split()) for _ in range(12)]
cnt = 0
while True:
    chain_effect = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != ".":
                chain_effect += BFS(i, j, board)
    if chain_effect == 0:
        break
    else:
        gravity(board)
        cnt += 1
print(cnt)