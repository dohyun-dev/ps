from collections import deque

def bfs(x, y):
    global answer
    q = deque([(x, y)])
    board[x][y] == "2"

    while q:
        x, y = q.popleft()

        for dx, dy in dir[x%2]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N+2 and 0 <= ny < M+2:
                if board[nx][ny] == "0":
                    board[nx][ny] = "2"
                    q.append((nx, ny))
                elif board[nx][ny] == "1":
                    answer += 1

M, N = map(int, input().split())
board = [["0"] * (M+2)] + [["0"] + input().split() + ["0"] for _ in range(N)] + [["0"] * (M+2)]
dir = {
    0: [(0, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)],
    1: [(0, 1), (1, 1), (1, 0), (0, -1), (-1, 0), (-1, 1)]
}
answer = 0
bfs(0, 0)
print(answer)