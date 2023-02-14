from collections import deque

M, N, H = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
q = deque([(h, i, j) for j in range(M) for i in range(N) for h in range(H) if board[h][i][j] == 1])
answer = -1

while q:
    for _ in range(len(q)):
        h, x, y = q.popleft()
        for nh, nx, ny in [(h-1, x, y), (h+1, x, y), (h, x-1, y), (h, x, y+1), (h, x+1, y), (h, x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and board[nh][nx][ny] == 0:
                board[nh][nx][ny] = 1
                q.append((nh, nx, ny))
    answer += 1
print(-1 if any(True for j in range(M) for i in range(N) for h in range(H) if board[h][i][j] == 0) else answer)