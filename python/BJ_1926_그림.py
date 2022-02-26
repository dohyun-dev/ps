import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def BFS(x, y, board):
    q = deque([(x, y)])    
    board[x][y] = "0"
    cnt = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
            dx = x + dx
            dy = y + dy
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == "1":
                board[dx][dy] = "0"
                q.append((dx,dy))
                cnt += 1
    return cnt     

n, m = map(int, input().split())
board = [list(input().split()) for _ in range(n)]
result = []

for i in range(n):
    for j in range(m):
        if board[i][j] == "1":
            result.append(BFS(i, j, board))

if result:  print(len(result), max(result), sep="\n")
else:   print(0, 0, sep="\n")
