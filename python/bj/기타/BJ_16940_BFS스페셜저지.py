import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque

N = int(input())
graph = defaultdict(list)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()

expected_value = [*map(int, input().split())]

if expected_value[0] != 1:
    print(0)
    sys.exit()

q = deque([1])
visited = [False] * (N + 1)
visited[1] = True
answer = 1
expected_value = expected_value[1:]
while q:
    temp = []
    cur = q.popleft()
    for next in graph[cur]:
        if not visited[int(next)]:
            visited[int(next)] = True
            temp.append(next)
    if temp:
        cur_len = len(temp)
        flag = False
        if temp != sorted(expected_value[:cur_len]):
            answer = 0
            break
        else:
            q.extend(expected_value[:cur_len])
            expected_value = expected_value[cur_len:]
print(answer)