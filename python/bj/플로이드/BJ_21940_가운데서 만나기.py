from posixpath import split
import sys; input = lambda : sys.stdin.readline().rstrip()
INF = 10000
N, M = map(int, input().split())
board = [[INF] * (N + 1) for _ in range(N + 1)]

# 간선 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    if board[a][b] > c:
        board[a][b] = c

for i in range(1, N+1):
    board[i][i] = 0
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j and board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
input()

result = [0] * (N + 1)
friends = list(map(int, input().split()))
for i in range(1, N+1):
    for f in friends:
        result[i] += board[i][f] + board[f][i]
        
min_dist = min(result[1:])
for i in range(1, N+1):
    if result[i] == min_dist:
        print(i, end=" ")