def check(x, y):
    tmp = [not visited[nx][ny] for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1, y), (x, y-1)] if 0 <= nx < N and 0 <= ny < N]
    return len(tmp) == 5 and all(tmp)

def flower(x, y, target):
    for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        visited[nx][ny] = target

def calc_cost(x, y):
    return sum(board[nx][ny] for nx, ny in [(x, y), (x-1, y), (x, y+1), (x+1, y), (x, y-1)])

def combi(l, r, c, total=0):
    global answer
    if l == 3:
        answer = min(answer, total)
        return
    for i in range(r, N):
        c = c if r == i else 1
        for j in range(c, N):
            if check(i, j):
                flower(i, j, 1)
                combi(l+1, r, c+1, total + calc_cost(i, j))
                flower(i, j, 0)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited= [[0] * N for _ in range(N)]
answer = float("inf")
combi(0, 0, 0)
print(answer)