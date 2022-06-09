import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def drop_cells():
    for j in range(10):
        stack = []
        for i in range(N):
            if board[i][j] != 0:
                stack.append(board[i][j])
        for i in range(N-1, -1, -1):
            if stack:
                board[i][j] = stack.pop()
            else:
                board[i][j] = 0

def BFS(x, y, target):
    q = deque([(x, y)])
    visited[x][y] = True
    temp = [(x, y)]

    while q:
        x, y = q.popleft()

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < 10 and board[nx][ny] == target and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                temp.append((nx, ny))

    if len(temp) >= K:
        for x, y in temp:
            board[x][y] = 0
        return True
    return False


N, K = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]

while True:
    flag = False
    visited = [[False] * 10 for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if board[i][j] != 0:
                tmp = BFS(i, j, board[i][j])
                if not flag and tmp:
                    flag = True
    if flag:
        drop_cells()
    else:
        break

for i in range(N):
    print("".join(map(str, board[i])))
