import sys; sys.setrecursionlimit(10**5)

def dfs(x=0, y=0):
    global answer
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            if board[nx][ny] == "0":
                dfs(nx, ny)
            elif board[nx][ny] == "1":
                board[nx][ny] = "0"
                answer -= 1

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
pre = answer = len([1 for i in range(N) for j in range(M) if board[i][j] == "1"])
time = 0
while answer != 0:
    pre, time = answer, time + 1
    visited = [[False] * M for _ in range(N)]
    dfs()
print(time, pre, sep="\n")


