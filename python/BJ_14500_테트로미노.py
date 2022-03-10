import sys; input = lambda : sys.stdin.readline().rstrip()

blocks = [
    [[1, 1, 1, 1]],
    [[1],[1],[1],[1]],
    [[1, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1], [0, 1], [0, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1], [1, 0], [1, 0]],
    [[1, 0, 0], [1, 1, 1]],
    [[1, 0], [1, 1], [0, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[0, 1], [1, 1], [1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[0, 1], [1, 1], [0, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[1, 0], [1, 1], [1, 0]]
]
    
N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
answer = 0

for block in blocks:
    for i in range(N):
        for j in range(M):
            if i + len(block) - 1 < N and j + len(block[0]) - 1 < M:
                temp = 0
                for x in range(len(block)):
                    for y in range(len(block[x])):
                        if block[x][y] == 1:
                            temp += board[i+x][j+y]
                answer = max(answer, temp)                
                
print(answer)