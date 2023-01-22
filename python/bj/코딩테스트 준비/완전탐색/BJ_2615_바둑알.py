import sys

board = [sys.stdin.readline().rstrip().split() for _ in range(19)]
dx, dy = [-1, 0, 1, 1], [1, 1, 1, 0]
cx, cy = [1, 0, -1, -1], [-1, -1, -1, 0]

for i in range(19):
    for j in range(19):
        if board[i][j] == '0':
            continue
        for d in range(4):
            target, cnt, nx, ny = board[i][j], 0, i, j
            while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target and cnt < 6:
                nx, ny = nx + dx[d], ny + dy[d]
                cnt += 1

            if cnt == 5:
                nx, ny = i + cx[d], j + cy[d]
                if 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == target:
                    continue
                print(target)
                print(i+1, j+1, sep=" ")
                exit()
print(0)