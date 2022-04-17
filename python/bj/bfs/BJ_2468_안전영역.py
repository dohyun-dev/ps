from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board, visited, rain):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] > rain:
                visited[nx][ny] = True
                q.append((nx, ny))

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
for rain in range(max(max(b) for b in board)):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > rain and not visited[i][j]:
                cnt += 1
                BFS(i, j, board, visited, rain)
    answer = max(answer , cnt)
print(answer)