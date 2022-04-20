from collections import deque


N, K = map(int, input().split())

if N == K:
    print(0)
    exit()

visited = [[-1] * 500001 for _ in range(2)]
visited[0][N] = 0

q = deque([N])
seconds = 0
while q:
    seconds += 1
    K += seconds
    if K > 500000:  break
    for _ in range(len(q)):
        cur = q.popleft()
        for next in [(cur-1), (cur + 1), (cur * 2)]:
            if 0 <= next <= 500000 and visited[seconds % 2][next] == -1:
                visited[seconds % 2][next] = seconds
                q.append(next)
        if visited[seconds % 2][K] != -1:
            print(seconds)
            exit()
print(-1)