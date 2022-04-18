from collections import deque


N, K = map(int, input().split())
board = [-1] * 100001
pre = [-1] * 100001
board[N] = 0
pre[N] = N

q = deque([N])
while q:
    cur = q.popleft()
    if cur == K:
        break
    for idx, next in enumerate([cur * 2, cur + 1, cur - 1]):
        if 0 <= next <= 100000 and board[next] == -1:
            pre[next] = cur
            board[next] = board[cur] + 1
            q.append(next)
cur = K
result = []
while cur != pre[cur]:
    result.append(str(cur))
    cur = pre[cur]
result.append(str(cur))
print(len(result) - 1)
print(" ".join(result[::-1]))