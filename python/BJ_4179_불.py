from collections import deque


R, C = map(int, input().split())
board = [list(*input().split()) for _ in range(R)]


j_q, f_q = deque(), deque()
dis_j, dis_f = [[-1] * C for _ in range(R)], [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if board[i][j] == "J":
            j_q.append((i, j))
            dis_j[i][j] = 0
        elif board[i][j] == "F":
            f_q.append((i, j))
            dis_f[i][j] = 0

while f_q:
    x, y = f_q.popleft()
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:    # 북 동 남 서
        dx = x + dx
        dy = y + dy
        if 0 <= dx < R and 0 <= dy < C and board[dx][dy] == "." and dis_f[dx][dy] == -1:
            dis_f[dx][dy] = dis_f[x][y] + 1
            f_q.append((dx,dy))


while j_q:
    x, y = j_q.popleft()
    for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:    # 북 동 남 서
        dx = x + dx
        dy = y + dy
        if 0 <= dx < R and 0 <= dy < C:
            if board[dx][dy] == "." and dis_j[dx][dy] == -1:
                if dis_f[dx][dy] == -1 or dis_j[x][y] + 1 < dis_f[dx][dy]:
                    dis_j[dx][dy] = dis_j[x][y] + 1
                    j_q.append((dx,dy))
        else:
            print(dis_j[x][y] + 1)
            exit(0)

print("IMPOSSIBLE")