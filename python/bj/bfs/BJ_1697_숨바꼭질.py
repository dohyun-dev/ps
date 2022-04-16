from collections import deque
N, K = map(int, input().split())
dist = [-1] * (100001)
dist[N] = 0
q = deque([N])
while q:
    cur = q.popleft()
    for next in [(cur-1), (cur+1), (cur*2)]:
        if 0 <= next <= 100000 and dist[next] == -1:
            dist[next] = dist[cur] + 1
            q.append(next)
print(dist[K])