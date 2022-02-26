import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def BFS(x, y, board, n):
    q = deque([(x, y)])
    board[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == 1:
                board[dx][dy] = 0
                q.append((dx, dy))
    

def solve(board, rain, n):
    check = [[0 if board[i][j] <= rain else 1 for j in range(n)] for i in range(n)]
    cnt = 0
    
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                cnt += 1
                BFS(i, j, check, n)
    
    return cnt        



if __name__ == "__main__":
    N = int(input())
    k = -sys.maxsize
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    
    for i in range(N):
        k = max(k, max(board[i]))


    for i in range(0, k+1):
        answer = max(answer, solve(board, i, N))

    print(answer)