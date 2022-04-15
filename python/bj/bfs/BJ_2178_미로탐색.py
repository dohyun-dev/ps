from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS():
    q = deque([(0, 0)])
    dist = [[-1] * M for _ in range(N)]
    dist[0][0] = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == '1' and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist[N-1][M-1]

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
print(BFS())