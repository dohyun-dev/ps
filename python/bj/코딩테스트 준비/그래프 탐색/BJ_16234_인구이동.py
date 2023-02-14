from collections import deque

def union(x, y):
    global flag
    q = deque([(x, y)])
    visited[x][y] = True
    union_list = [(x, y)]
    total = board[x][y]

    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    continue
                if not(L <= abs(board[x][y] - board[nx][ny]) <= R):
                    continue
                visited[nx][ny] = True
                union_list.append((nx, ny))
                total += board[nx][ny]
                q.append((nx, ny))

    if len(union_list) > 1:
        flag = True
        for x, y in union_list:
            board[x][y] = total // len(union_list)
    else:
        cache_temp.append(union_list.pop())

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cache = [(i, j) for i in range(N) for j in range(i % 2, N, 2)]
flag, answer = True, -1

while flag:
    flag, cache_temp = False, []
    visited = [[False] * N for _ in range(N)]
    for x, y in cache:
        if visited[x][y]:
            continue
        union(x, y)
    answer += 1
print(answer)