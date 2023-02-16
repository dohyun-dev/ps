from collections import deque


N, K = map(int, input().split())
sam, houses = [*map(int, input().split())], []
visited, answer = set(sam), 0

q = deque((s, 1) for s in sam)
while q:
    x, dist = q.popleft()

    for nx in [(x - 1), (x + 1)]:
        if nx not in visited:
            visited.add(nx)
            answer, K = answer + dist, K - 1
            q.append((nx, dist + 1))
        if K == 0:
            q = []
            break
print(answer)