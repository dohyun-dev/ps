def bfs(x, y, board, m, n):
    tmp = []

    for i in range(x, min(x+2, m)):
        for j in range(y, min(y+2, n)):
            if board[x][y] == board[i][j]:
                tmp.append((i, j))
    if len(tmp) == 4:
        return tmp
    else:
        return []


def drop(board, m, n):
    for y in range(n):
        stack = []
        for x in range(m):
            if board[x][y] != 0:
                stack.append(board[x][y])

        for x in range(m - 1, -1, -1):
            if stack:
                board[x][y] = stack.pop()
            else:
                board[x][y] = 0


def solution(m, n, board):
    flag = True
    board = [list(b) for b in board]
    while flag:
        delete_list = []
        for i in range(m):
            for j in range(n):
                if board[i][j] != 0:
                    temp = bfs(i, j, board, m, n)
                    delete_list.extend(temp)
        for x, y in delete_list:
            board[x][y] = 0
        drop(board, m, n)
        if not delete_list:
            flag = False

    return sum([sum([1 if board[i][j] == 0 else 0 for j in range(n)]) for i in range(m)])

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))