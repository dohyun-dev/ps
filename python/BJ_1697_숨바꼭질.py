from collections import deque
from operator import ne
import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())

def bfs():
    q = deque([N])
    dist = [0] * 100001
    while q:
        cur = q.popleft()
        if cur == K:   return dist[cur]
        for next in [cur - 1, cur + 1, cur * 2]:
            if 0 <= next <= 100000 and not dist[next]:
                dist[next] = dist[cur] + 1
                q.append(next)
        
print(bfs())