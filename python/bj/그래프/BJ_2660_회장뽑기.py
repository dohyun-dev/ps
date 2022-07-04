import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def BFS(cur):
    q = deque([cur])
    visited = [False] * (N + 1)
    visited[cur] = True
    score = 0
    cnt = 1

    while q:
        if cnt == N:
            break
        for _ in range(len(q)):
            cur = q.popleft()
            for next_node in graph[cur]:
                if not visited[next_node]:
                    visited[next_node] = True
                    cnt += 1
                    q.append(next_node)
        score += 1
    return score

N = int(input())
graph = {i: [] for i in range(1, N+1)}
score_arr = [0] * (N + 1)

while (data := tuple(map(int, input().split()))) != (-1, -1):
    a, b = data
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    score_arr[i] = BFS(i)

result_score = min(score_arr[1:])
answer = [idx for idx, score in enumerate(score_arr[1:], 1) if score == result_score]
print(result_score, len(answer))
print(*answer)