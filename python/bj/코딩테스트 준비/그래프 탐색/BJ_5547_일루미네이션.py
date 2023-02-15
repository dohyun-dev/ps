import sys; sys.setrecursionlimit(10**5)

def dfs(x, y):
    for X, Y in d[x % 2]:
        nx, ny = x + X, y + Y
        if 0 <= nx < N+2 and 0 <= ny < M+2:
            if map[nx][ny] == 0:
                map[nx][ny] = 2
                dfs(nx, ny)
            if map[nx][ny] == 1:
                cnt[0] += 1

M, N = map(int, input().split())
map = [[0] * (M + 2)] + [[0] + [*map(int, input().split())] + [0] for _ in range(N)] + [[0] * (M + 2)]
d = {0: [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)], 1: [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1)]}
cnt, map[0][0] = [0], 2
dfs(0, 0)
print(cnt[0])