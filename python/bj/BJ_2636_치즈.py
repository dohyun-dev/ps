from collections import deque

# 접촉면 탐색
def BFS1():
    q = deque([(0, 0)])
    visited = [[0] * M for _ in range(N)]
    
    while q:
        x, y = q.popleft()
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 2
                q.append((nx, ny))
    
    return visited

def BFS2(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    tmp = []
    cnt = 0
    
    while q:
        x, y = q.popleft()
        flag = False
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                if visited[nx][ny] == 2:
                    flag = True
        if flag:
            cnt += 1
            tmp.append((x, y))
    
    for tx, ty in tmp:
        board[tx][ty] = 0
        
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cnt += 1
    return cnt
                
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0
result = [0]


while True:
    flag = True
    visited = BFS1()
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 :
                flag = False
                cnt += 1
                for nx, ny in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                    if visited[nx][ny] == 2:
                        board[i][j] = 0
                        break
    if flag:
        break
    result.append(cnt)
    time += 1

print(time)
print(result[-1])