import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
board = [list(*input().split()) for _ in range(N)]

ch1 = [[0] * N for _ in range(N)]
ch2 = [[0] * N for _ in range(N)]
cnt1 = 0    # 정상
cnt2 = 0    # 색약

# 색맹이 아닐때
def BFS(x, y):
    q = deque([(x,y)])
    
    ch1[x][y] = cnt1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < N and not ch1[nx][ny] and board[x][y] == board[nx][ny]:
                ch1[nx][ny] = cnt1
                q.append((nx,ny))

def BFS2(x, y):
    q = deque([(x,y)])
    ch2[x][y] = cnt2
    
    if board[x][y] in "RG":
        comp = "RG"     
    else:
        comp = "B"
    
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < N and 0 <= ny < N:
                if not ch2[nx][ny] and board[nx][ny] in comp:
                    ch2[nx][ny] = cnt2
                    q.append((nx,ny))

for i in range(N):
    for j in range(N):
        if not ch1[i][j]:
            cnt1 += 1
            BFS(i, j)
        if not ch2[i][j]:
            cnt2 += 1
            BFS2(i, j)
            
print(cnt1, cnt2)