from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board):
    q = deque([(x, y)])
    color = board[x][y]
    board[x][y] = 'X'
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == color:
                board[nx][ny] = 'X'
                q.append((nx, ny))

def BFS2(x, y, board):
    q = deque([(x, y)])
    color = board[x][y]
    board[x][y] = 'X'
    
    if color == 'R' or color == 'G':
        color = {"R", "G"}
    else:
        color = {"B"}
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in color:
                board[nx][ny] = 'X'
                q.append((nx, ny))

# 적록 색약이 아닐때
def solution1(board):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 'X':
                cnt += 1
                BFS(i, j, board)
    return cnt
                
# 적록 색약일 때
def solution2(board):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != 'X':
                cnt += 1
                BFS2(i, j, board)
    return cnt
                
N = int(input())
board = [list(input()) for _ in range(N)]
print(solution1([b[:] for b in board]), solution2([b[:] for b in board]))