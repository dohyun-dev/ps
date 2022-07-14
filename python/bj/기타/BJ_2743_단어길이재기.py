import sys; input = lambda : sys.stdin.readline().rstrip()
from itertools import combinations
from collections import deque

def bfs(q: deque):
    dist = [[-1] * N for _ in range(N)]
    result = -1

    for x, y in q:
        dist[x][y] = 0

    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y),(x, y+1),(x+1, y),(x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1 and board[nx][ny] != 1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    for i in range(N):
        for j in range(N):
            if board[i][j] != 1:
                if dist[i][j] == -1:
                    return sys.maxsize
                else:
                    result = max(result, dist[i][j])
    return result

N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
virus_list = []
answer = sys.maxsize

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus_list.append((i, j))

for l in combinations(virus_list, M):
    answer = min(answer, bfs(deque(l)))

print(answer if answer != sys.maxsize else -1)
