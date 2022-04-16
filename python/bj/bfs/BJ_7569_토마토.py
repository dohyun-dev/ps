from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

M, N, H = map(int, input().split())
board = [[input().split() for _ in range(N)] for _ in range(H)]
q = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == '1':
                q.append((i, j, k))
level = 0

while q:
    for _ in range(len(q)):
        h, x, y = q.popleft()
        
        for nh, nx, ny in [(h-1, x, y), (h+1, x, y), (h, x-1, y), (h, x, y+1), (h, x+1, y), (h, x, y-1)]:
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and board[nh][nx][ny] == '0':
                board[nh][nx][ny] = '1'
                q.append((nh, nx, ny))
    level += 1

for i in range(H):
    flag = False
    for j in range(N):
        for k in range(M):
            if board[i][j][k] == '0':
                flag = True
                break
        if flag:    break
    if flag: break
else:
    print(level-1)
    exit()
print(-1)