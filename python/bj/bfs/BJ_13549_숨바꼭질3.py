from collections import deque


N, K = map(int, input().split())
board = [-1] * 100001
board[N] = 0

q = deque([N])
while q:
    cur = q.popleft()
    
    for idx, next in enumerate([cur * 2, cur + 1, cur - 1]):
        if 0 <= next <= 100000:
            if idx == 0:
                if board[next] == -1 or board[cur] < board[next]:
                    board[next] = board[cur]
                    q.append(next)
            else:
                if board[next] == -1 or board[cur] + 1 < board[next]:
                    board[next] = board[cur] + 1
                    q.append(next)
print(board[K])
