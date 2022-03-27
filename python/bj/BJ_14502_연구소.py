from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS():
    q = deque(virus)
    board2 = [board[i][:] for i in range(N)]
    while q:
        x, y = q.popleft()
         
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and board2[nx][ny] == "0":
                board2[nx][ny] = "2"
                q.append((nx, ny))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board2[i][j] == "0":  cnt += 1
    return cnt            

def DFS(cnt, r, c):
    global result
    if cnt == 3:
        result = max(result, BFS())
        return
    for i in range(r, N):
        if i == r:
            c2 = c
        else:
            c2 = 0
        for j in range(c2, M):
            if board[i][j] == "0":
                board[i][j] = "1"
                DFS(cnt+1, i, j+1)
                board[i][j] = "0"

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    result = -sys.maxsize

    virus = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == "2":
                virus.append((i, j))
    DFS(0, 0, 0)
    print(result)