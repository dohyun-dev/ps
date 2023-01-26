import sys; input = sys.stdin.readline

def dfs(x, y, total, cnt=0):
    global answer
    if cnt == 3:
        answer = max(answer, total)
        return
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            if cnt == 1:
                visited[nx][ny] = 1
                dfs(x, y, total + board[nx][ny], cnt+1)
                visited[nx][ny] = 0
            visited[nx][ny] = 1
            dfs(nx, ny, total + board[nx][ny], cnt+1)
            visited[nx][ny] = 0


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, board[i][j])
        visited[i][j] = 0
print(answer)