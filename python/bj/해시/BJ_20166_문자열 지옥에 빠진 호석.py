import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque, Counter


def bfs(x, y, path, string):
    q = deque([(x, y, path, string)])
    cnt = 0

    while q:
        x, y, path, string = q.popleft()
        word_dict[string] += 1
        for nx, ny in [(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]:
            if len(string) + 1 > 5:
                break

            if nx < 0:
                nx = N + nx
            if ny < 0:
                ny = M + ny

            nx, ny = nx % N, ny % M
            next_path = path+f'({nx},{ny})'

            if next_path not in check:
                check.add(next_path)

                q.append((nx, ny, next_path, string+board[nx][ny]))
    return cnt


N, M, K = map(int, input().split())
board = [input() for _ in range(N)]
check = set()
word_dict = Counter()

for i in range(N):
    for j in range(M):
        if f'({i},{j})' not in check:
            check.add(f'({i},{j})')
            bfs(i, j, f'({i},{j})', board[i][j])

for _ in range(K):
    print(word_dict[input()])