import sys; input = lambda : sys.stdin.readline().rstrip()

result = []
for t in range(1, int(input())+1):
    N = int(input())
    line = 0
    board = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if board[i][j]: cores.append((i, j))
    result.append(f'#{t} {line}')
print("\n".join(result))