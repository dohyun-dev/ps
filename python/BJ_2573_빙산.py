import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def melt(x, y, melt_list):
    cnt = 0
    for dx, dy in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                cnt += 1
    if board[x][y] - cnt > 0:
        board[x][y] -= cnt
    else:
        return melt_list.append((x, y))
        
def area_check(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0), (0, 1), (1, 0), (0, -1)]:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] > 0:
                visited[nx][ny] = True
                q.append((nx, ny))

def check():
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] > 0:
                area_check(i, j, visited)
                cnt += 1
        
    if cnt >= 2:
        return False
    return True
            
            
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
year = 0

while check():
    visited = [[False] * M for _ in range(N)]
    flag = False
    melt_list = []
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j] > 0:
                flag = True
                visited[i][j] = True
                melt(i, j, melt_list)
    
    for x, y in melt_list:
        board[x][y] = 0    
    year += 1
    if not flag:
        year = 0
        break
print(year)