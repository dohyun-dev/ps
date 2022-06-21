from re import L
import sys; input = lambda : sys.stdin.readline().rstrip()

# 치킨집의 좌표와 집의 좌표를 구하는 함수
def search(board):
    chicken = []
    home = []
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                home.append((i, j))
            elif board[i][j] == 2:
                chicken.append((i, j))
    return (chicken, home)

def calc(chicken, home):
    sum = 0
    for h in home:
        min_dist = sys.maxsize
        for c in chicken:
            min_dist = min(min_dist, abs(c[0] - h[0]) + abs(c[1] - h[1]))
        sum += min_dist
    return sum

set = []
def DFS(cnt=0, start=0):
    global result
    if cnt != 0:
        result = min(result, calc(set, home))
    if cnt == M:
        return
    for i in range(start, len(chicken)):
        set.append(chicken[i])
        DFS(cnt+1, i+1)
        set.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    chicken, home = search(board)
    result = sys.maxsize
    
    DFS()
    print(result)