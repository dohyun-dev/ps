import sys; input = lambda : sys.stdin.readline().rstrip()
INF = 1000000
N, M = int(input()), int(input())
board = [[INF] * (N + 1) for _ in range(N + 1)]
path = [[-1] * (N + 1) for _ in range(N + 1)]

# 간선 초기화
for _ in range(M):
    a, b, c = map(int, input().split())
    if board[a][b] > c:
        board[a][b] = c
        path[a][b] = a

for i in range(1, N+1):
    if board[i][i] == INF:
        board[i][i] = 0
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j and board[i][j] > board[i][k] + board[k][j]:
                board[i][j] = board[i][k] + board[k][j]
                path[i][j] = path[k][j]
            
print("\n".join(" ".join(str(node) for node in b[1:]) for b in board[1:]))
for i in range(1, N+1):
    for j in range(1, N+1):
        if path[i][j] == -1:
            print(0)
        else:
            answer = [j]
            end = j
            while i != end:
                answer.append(path[i][end])
                end = path[i][end]
            print(len(answer), end=" ")
            print(*map(str, answer[::-1]))