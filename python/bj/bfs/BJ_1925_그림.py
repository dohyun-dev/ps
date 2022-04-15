from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board):
    q = deque([(x, y)])
    board[x][y] = '0'
    cnt = 1
    while q:
        x, y = q.popleft()
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '1':
                cnt += 1
                board[nx][ny] = '0'
                q.append((nx, ny))
    return cnt

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
cnt, max_result = 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == '1':
            cnt += 1
            max_result = max(max_result, BFS(i, j, board))
            
print(cnt, max_result, sep="\n")

