from collections import deque

def check(x, y):
    if x+H > N or y+W > M:
        return False
    return all(False for wx, wy in walls if x <= wx < x+H and y <= wy < y+W)

def bfs(x, y):
    q = deque([(x, y, 0)])
    board[x][y] = "2"
    while q:
        x, y, cnt = q.popleft()
        if x == fr and y == fc:
            return cnt
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "0" and check(nx, ny):
                board[nx][ny] = "2"
                q.append((nx, ny, cnt+1))
    return -1

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
walls = set((i, j) for i in range(N) for j in range(M) if board[i][j] == "1")
H, W, sr, sc, fr, fc = map(int, input().split())
sr, sc, fr, fc = sr-1, sc-1, fr-1, fc-1
print(bfs(sr, sc))
