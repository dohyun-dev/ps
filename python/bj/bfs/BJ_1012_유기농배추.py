from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, board):
    q = deque([(x, y)])
    board[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 1:
                board[nx][ny] = 0
                q.append((nx, ny))

result = []
for _ in range(int(input())):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    answer = 0
    for _ in range(K):
        a, b = map(int, input().split())
        board[a][b] = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                answer += 1
                BFS(i, j, board)  
    result.append(str(answer))
print("\n".join(result))