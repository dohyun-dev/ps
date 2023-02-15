from collections import deque

def bfs(x, y):
    global answer
    q = deque([(x, y)])
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for nx, ny in [
            [(x, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y)],
            [(x, y + 1), (x + 1, y + 1), (x + 1, y), (x, y - 1), (x - 1, y), (x - 1, y + 1)]
        ][x % 2]:
            if 0 <= nx < N+2 and 0 <= ny < M+2:
                if visited[nx][ny]:
                    continue

                if board[nx][ny] == "0":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                else:
                    answer += 1

M, N = map(int, input().split())
board = [["0"] * (M+2)] + [["0"] + input().split() + ["0"] for _ in range(N)] + [["0"] * (M+2)]
visited = [[False] * (M+2) for _ in range(N+2)]
answer = 0
bfs(0, 0)
print(answer)