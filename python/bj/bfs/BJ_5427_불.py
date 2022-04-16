import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

result = []
for _ in range(int(input())):
    M, N = map(int, input().split())
    board = [list(input()) for _ in range(N)]
    
    f_q = deque()
    q = deque()
    f_dist = [[-1] * M  for _ in range(N)]
    dist = [[-1] * M  for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == '@':
                dist[i][j] = 0
                q.append((i, j))
            if board[i][j] == '*':
                f_dist[i][j] = 0
                f_q.append((i, j))
    
    for x, y in f_q:    f_dist[x][y] = 0
    for x, y in q:      dist[x][y] = 0
    
    while f_q:
        x, y = f_q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and f_dist[nx][ny] == -1 and board[nx][ny] != '#':
                f_dist[nx][ny] = f_dist[x][y] + 1
                f_q.append((nx, ny))
    
    flag = False
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] != '#' and dist[nx][ny] == -1:
                    if f_dist[nx][ny] == -1 or f_dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))
            else:
                result.append(str(dist[x][y] + 1))
                flag = True
                break
        if flag:    break
    
    if not flag:    result.append("IMPOSSIBLE")
print("\n".join(result))
