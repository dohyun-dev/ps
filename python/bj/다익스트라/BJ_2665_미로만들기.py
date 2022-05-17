import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop


def bfs(x=0, y=0):
    q = [(0, x, y)]
    dist = [[-1] * N for _ in range(N)]
    dist[x][y] = 0
    
    while q:
        cost, x, y = heappop(q)
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                if board[nx][ny] == '0':
                    dist[nx][ny] = cost + 1
                    heappush(q, (cost+1, nx, ny))
                else:
                    dist[nx][ny] = cost
                    heappush(q, (cost, nx, ny))
    return dist[N-1][N-1]
        
N = int(input())
board = [list(input()) for _ in range(N)]
print(bfs())

