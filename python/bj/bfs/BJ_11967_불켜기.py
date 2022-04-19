import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque

def on_switch(x, y):
    global answer
    if (x, y) in switchs:
        cnt = 0
        for nx, ny in switchs[(x, y)]:
            if board[nx][ny] != 1:
                board[nx][ny] = 1
                cnt += 1
                answer += 1
        if cnt > 0:
            return True
        return False
    return False

N, M = map(int, input().split())
switchs = defaultdict(list)
for _ in range(M):
    a, b, c, d = map(int, input().split())
    switchs[(a, b)].append((c, d))

board = [[0] * (N + 1) for _ in range(N+1)]
visited = [[False] * (N + 1) for _ in range(N+1)]
answer = 1

board[1][1] = 1
visited[1][1] = True
on_switch(1, 1)

q = deque([(1, 1)])
while q:
    x, y = q.popleft()
    
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 < nx <= N and 0 < ny <= N and not visited[nx][ny] and board[nx][ny] == 1:
            if on_switch(nx, ny):
                visited = [[False] * (N + 1) for _ in range(N+1)]
            visited[nx][ny] = True
            q.append((nx, ny))
print(answer)