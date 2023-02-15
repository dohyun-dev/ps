from collections import deque

N, K = map(int, input().split())
board = [-1] * (10**5+1)
q = deque([N])
board[N] = 0
while q:
    x = q.popleft()
    for idx, next in enumerate([x-1, x+1, x*2]):
        next_cnt = board[x] if idx == 2 else board[x] + 1
        if 0 <= next < 10**5+1:
            if not(board[next] == -1 or (board[next] != -1 and board[next] > next_cnt)):
                continue
            board[next] = next_cnt
            q.append(next)
print(board[K])