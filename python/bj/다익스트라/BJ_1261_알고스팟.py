import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

M, N = map(int, input().split())
board = [list(input()) for _ in range(N)]

dist = [[-1] * M for _ in range(N)]
dist[0][0] = 0
q = [(0, 0, 0)]

while q:
    cnt, x, y = heappop(q)
    
    if x == N-1 and y == M-1:
        print(cnt)
        sys.exit()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            if board[nx][ny] == '1':
                dist[nx][ny] = cnt + 1
                heappush(q, (cnt+1, nx, ny))
            else:
                dist[nx][ny] = cnt + 1
                heappush(q, (cnt, nx, ny))
print(-1)