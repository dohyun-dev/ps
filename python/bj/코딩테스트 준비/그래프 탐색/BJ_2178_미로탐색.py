from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
q = deque([(0, 0, 1)])
while q:
    x, y, cnt = q.popleft()

    if x == N-1 and y == M-1:
        print(cnt)
        exit()

    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1":
            board[nx][ny] = "0"
            q.append((nx, ny, cnt+1))