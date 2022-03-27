import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x = 0, y = 0):
    q = deque([(x,y)])
    cnt = 1
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if x == N-1 and y == M-1:
                return cnt
            if board[x][y] == "0":  continue
            board[x][y] = "0"
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1":
                    q.append((nx, ny))
        cnt += 1
        
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(*input().split()) for _ in range(N)]
    
    print(BFS())
    
                