from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
dist = [0] * 100001
visited = [None] * 100001
visited[N] = N
q = deque([N])

while q:
    cur = q.popleft()
    
    if cur == K:
        break;
    
    if 0 <= cur * 2 < 100001 and (visited[cur * 2] == None or dist[cur] < dist[cur * 2]):
        # 비지트 불린 대신 현재 위치를 넣음
        visited[cur * 2] = cur
        dist[cur * 2] = dist[cur]
        q.append(cur * 2)
    for next in [cur + 1, cur - 1]:
        if 0 <= next < 100001 and (visited[next] == None or dist[cur] < dist[next]):
            # 비지트 불린 대신 현재 위치를 넣음
            visited[next] = cur
            dist[next] = dist[cur] + 1
            q.append(next)

result = []
path = K
while visited[path] != path:
    result.append(path)
    path = visited[path]
result.append(N) 
print(dist[K])

# 경로 출력 코드
# print(result[::-1])