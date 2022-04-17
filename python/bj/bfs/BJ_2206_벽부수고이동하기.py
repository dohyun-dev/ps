from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def bfs():
    q = deque([(0, 0, 0)])
    dist = [[[0] * M for _ in range(N)] for _ in range(2)]
    dist[0][0][0] = 1
    while q:
        l, x, y = q.popleft()
        if x == N-1 and y == M-1:
            return dist[l][x][y]
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '1' and l+1 <= 1 and dist[l+1][nx][ny] == 0:
                    dist[l+1][nx][ny] = dist[l][x][y] + 1
                    q.append((l+1, nx, ny))
                elif board[nx][ny] == '0' and dist[l][nx][ny] == 0:
                    dist[l][nx][ny] = dist[l][x][y] + 1
                    q.append((l, nx, ny))
    return -1            

N, M = map(int, input().split())
board =[input() for _ in range(N)]
print(bfs())