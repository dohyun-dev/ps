from collections import deque

result = []
for t in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, *input().split())) for _ in range(N)]
    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0
    
    q = deque([(0, 0, 0)])
    
    while q:
        x, y, c = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N:
                next_cost = dist[x][y] + board[nx][ny]
                if next_cost < dist[nx][ny]:
                    dist[nx][ny] = next_cost
                    q.append((nx, ny, next_cost))
    
    result.append(f'#{t} {dist[N-1][N-1]}')
print("\n".join(result))
    
    