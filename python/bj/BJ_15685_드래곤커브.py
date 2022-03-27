import sys; input = lambda : sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())

board = [[5] * (N+1) for _ in range(N+1)]
a = [[0] * (N + 1)]
visited = [[[] for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1): 
    a.append([0] + list(map(int, input().split())))

for _ in range(M):  
    x, y, level = map(int, input().split())
    visited[x][y].append(level)


for _ in range(K):
    # 봄
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j]:
                temp, summer_dead = [], 0
                visited[i][j].sort()
                for k, val in enumerate(visited[i][j]):
                    # 어린 나무 양분을 먹어준다
                    if board[i][j] >= val:
                        temp.append(val + 1)
                        board[i][j] -= val
                    else:
                        # 여름처리
                        summer_dead += val // 2
                board[i][j] += summer_dead
                visited[i][j] = temp[:]
    # 가을
    for i in range(1, N+1):
        for j in range(1, N+1):
            if visited[i][j]:
                for k, val in enumerate(visited[i][j]):
                    if val % 5 == 0:
                        for nx, ny in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
                            if 1 <= nx <= N and 1 <= ny <= N:
                                visited[nx][ny].append(1)
    # 겨울
    for i in range(1, N+1):
        for j in range(1, N+1):
            board[i][j] += a[i][j]

answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if visited[i][j]:
            answer += len(visited[i][j])
print(answer)