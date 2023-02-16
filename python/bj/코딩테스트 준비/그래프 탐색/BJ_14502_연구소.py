from collections import deque

def calc():
    q = deque(virus_list)
    visited = [[False] * M for _ in range(N)]

    for x, y in q:
        visited[x][y] = True

    while q:
        x, y = q.popleft()

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "0" and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return len([1 for i in range(N) for j in range(M) if board[i][j] == "0" and not visited[i][j]])

def combi(x=0, y=0, cnt=0):
    global answer
    if cnt == 3:
        answer = max(answer, calc())
        return
    for i in range(x, N):
        y = y if i == x else 0
        for j in range(y, M):
            if board[i][j] != "0":
                continue
            board[i][j] = "1"
            combi(i, j+1, cnt+1)
            board[i][j] = "0"

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
virus_list = [(i, j) for i in range(N) for j in range(M) if board[i][j] == "2"]
answer = 0
combi()
print(answer)