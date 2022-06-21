import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def BFS(x, y):
    q = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    board[x][y] = 2
    while q:
        x, y = q.popleft()
        for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= dx < N and 0 <= dy < M:
                if board[dx][dy] == 0 or board[dx][dy] == 2:
                    if not visited[dx][dy]:
                        visited[dx][dy] = True
                        board[dx][dy] = 2
                        q.append((dx, dy))
                    
def BFS2(x, y, visited, erase):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        cnt = 0
        for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= dx < N and 0 <= dy < M:
                if board[dx][dy] == 1 and not visited[dx][dy]:
                    visited[dx][dy] = True
                    q.append((dx, dy))
                if board[dx][dy] == 2:
                    cnt += 1
        if cnt >= 2:
            erase.append((x,y))
                    
cnt = 0
while True:
    BFS(0, 0)
    erase = []
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visited[i][j]:
                BFS2(i, j, visited, erase)
    if not erase:
        break
    else:
        for x, y in erase:
            board[x][y] = 2
        cnt += 1
print(cnt)
