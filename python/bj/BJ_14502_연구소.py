from collections import deque
from copy import deepcopy
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS():
    check = [board[i][:] for i in range(N)]
    q = deque(viruses)
    answer = 0
    
    while q:
        vx, vy = q.popleft()
        
        for nx, ny in [(vx-1, vy), (vx, vy+1), (vx+1, vy), (vx, vy-1)]:
            if 0 <= nx < N and 0 <= ny < M and check[nx][ny] == '0':
                check[nx][ny] = '2'
                q.append((nx, ny))
        
    for i in range(N):
        for j in range(M):
            if check[i][j] == '0':
                answer += 1
    return answer

def wall(r, c, cnt = 0):
    global answer
    if cnt == 3:
        answer = max(answer, BFS())
        return
    for i in range(r, N):
        if i == r:  c1 = c
        else:   c1 = 0
        for j in range(c1, M):
            if board[i][j] == '0':
                board[i][j] = '1'
                wall(i, j + 1, cnt + 1)
                board[i][j] = '0'
            
N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
viruses = []
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '2':
            viruses.append((i, j))
wall(0, 0)
print(answer)