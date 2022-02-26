import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

m, n = map(int, input().split())
board = [list(input().split()) for _ in range(n)]

def BFS():
    q = deque()    
   
    for i in range(n):
        for j in range(m):
            if board[i][j] == "1":
                q.append((i, j))
    
    if len(q) == n * m: return 0
    
    cnt = 0
    while q:
        size = len(q)
        for _ in range(size):
            x, y = q.popleft()
            for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
                dx = x + dx
                dy = y + dy
                if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == "0":
                    board[dx][dy] = "1"
                    q.append((dx,dy))  
        cnt += 1
    cnt -= 1
    for i in range(n):
        for j in range(m):
            if board[i][j] == "0":
                return -1   
    else: return cnt
            
print(BFS())