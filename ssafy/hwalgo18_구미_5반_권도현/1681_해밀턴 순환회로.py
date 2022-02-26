import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, start = 0, sum=0):
    global result
    if sum >= result:
        return
    if l == N-1:
        if board[start][0] != 0:
            result = sum + board[start][0]
        return
    for i in range(1, N):
        if not check[i] and board[start][i] != 0:
            check[i] = True
            DFS(l+1, i, sum + board[start][i])
            check[i] = False
            
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
check[0] = True
result = sys.maxsize
DFS()
print(result)