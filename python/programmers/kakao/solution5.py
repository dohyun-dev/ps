def shift_row(rc, N, M):
    return [rc[-1]] + rc[:-1]

def rotate(rc, N, M):
    first = rc[0][0]
    for r in range(N-1):
        rc[r][0] = rc[r+1][0]
    for c in range(M-1):
        rc[N-1][c] = rc[N-1][c+1]
    for r in range(N-1, 0, -1):
        rc[r][M-1] = rc[r-1][M-1]
    for c in range(M-1, 1, -1):
        rc[0][c] = rc[0][c-1]
    rc[0][1] = first

def solution(rc, operations):
    N, M = len(rc), len(rc[0])
    for operation in operations:
        if operation == "Rotate":
            rotate(rc, N, M)
        else:
            rc = shift_row(rc, N, M)
    return rc

solution([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], ["ShiftRow", "Rotate", "ShiftRow", "Rotate"])