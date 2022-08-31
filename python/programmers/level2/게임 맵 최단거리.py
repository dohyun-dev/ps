from collections import deque

def bfs(x, y, maps, N, M):
    q = deque([(x, y)])
    dist = [[-1] * M for _ in range(N)]
    dist[x][y] = 1

    while q:
        x, y = q.popleft()
        for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                maps[nx][ny] = 0
                q.append((nx, ny))
    return dist[N-1][M-1]

def solution(maps):
    return bfs(0, 0, maps, len(maps), len(maps[0]))