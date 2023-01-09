dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def dfs(l=0, cnt=0, connect=0):
    global answer, max_connect
    if l == len(cores):
        if connect > max_connect:
            answer, max_connect = cnt, connect
        elif connect == max_connect:
            answer = min(answer, cnt)
        return
    x, y = cores[l]
    for i in range(4):
        nx, ny, flag = x, y, False
        tmp = []
        while True:
            nx, ny = nx + dx[i], ny + dy[i]
            if not (0 <= nx < N) or not (0 <= ny < N):
                flag = True
                break
            if board[nx][ny] == 1 or lines[nx][ny]:
                break
            tmp.append((nx, ny))

        if flag:
            for tx, ty in tmp:
                lines[tx][ty] = True

            dfs(l + 1, cnt + len(tmp), connect+1)

            for tx, ty in tmp:
                lines[tx][ty] = False
    dfs(l+1, cnt, connect)

for t in range(1, int(input())+1):
    answer, max_connect = float("inf"), 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = [(i, j) for j in range(1, N-1) for i in range(1, N-1) if board[i][j] == 1]
    lines = [[False] * N for _ in range(N)]

    dfs()
    print('#{} {}'.format(t, answer))