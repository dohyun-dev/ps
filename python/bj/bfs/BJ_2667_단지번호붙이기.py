from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board):
    q = deque([(x, y)])
    board[x][y] = '0'
    cnt = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == '1':
                cnt += 1
                board[nx][ny] = '0'
                q.append((nx, ny))
    return str(cnt)

N = int(input())
board = [list(input()) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            result.append(BFS(i, j, board))

print(len(result))
print("\n".join(sorted(result, key=lambda x: int(x))))