import sys
from collections import deque

def turn_row(idx, board):
    board = convert_list(board)
    for i in range(3):
        board[idx][i] = "T" if board[idx][i] == "H" else "H"
    return convert_str(board)


def turn_col(idx, board):
    board = convert_list(board)
    for i in range(3):
        board[i][idx] = "T" if board[i][idx] == "H" else "H"
    return convert_str(board)


def turn_left_diagonal(board):
    board = convert_list(board)
    for i in range(3):
        board[i][i] = "T" if board[i][i] == "H" else "H"
    return convert_str(board)


def turn_right_diagonal(board):
    board = convert_list(board)
    for i in range(3):
        board[i][3 - i - 1] = "T" if board[i][3 - i - 1] == "H" else "H"
    return convert_str(board)


def convert_str(board):
    return "".join("".join(b) for b in board)

def convert_list(board):
    return [list(board[:3]),
            list(board[3:6]),
            list(board[6:9])]

for _ in range(int(sys.stdin.readline())):
    board = [sys.stdin.readline().split() for _ in range(3)]
    q = deque([(0, convert_str(board))])
    check = set()
    flag = False
    answer = -1

    while q:
        cnt, cur = q.popleft()
        check.add(cur)

        if len(set(cur)) == 1:
            answer = cnt
            break

        if len(check) == 512:
            break

        for i in range(3):
            tmp = turn_row(i, cur)
            if tmp not in check:
                q.append((cnt+1, tmp))
            tmp = turn_col(i, cur)
            if tmp not in check:
                q.append((cnt+1, tmp))

        tmp = turn_left_diagonal(cur)
        if tmp not in check:
            q.append((cnt + 1, tmp))

        tmp = turn_right_diagonal(cur)
        if tmp not in check:
            q.append((cnt + 1, tmp))

    print(answer)

