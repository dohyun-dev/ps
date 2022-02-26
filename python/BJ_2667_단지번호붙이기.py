import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y, board):
    q = deque([(x, y)])
    cnt = 0
    
    while q:
        x, y = q.popleft()
        if board[x][y] == "0":  continue
        board[x][y] = "0"
        cnt+=1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == "1":
                q.append((nx, ny))
    return cnt

if __name__ == "__main__":
    N = int(input())
    board = [list(*input().split()) for _ in range(N)]
    result = []
    
    for i in range(N):
        for j in range(N):
            if board[i][j] == "1":
                result.append(BFS(i, j, board))
    
    print(len(result))
    for i in sorted(result):
        print(i)
                