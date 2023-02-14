from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
q = deque([(i, j) for j in range(M) for i in range(N) if board[i][j] == 1])
answer = -1

while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
    answer += 1
print(-1 if any(any(map(lambda x: x==0, b)) for b in board) else answer)