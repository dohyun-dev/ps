from collections import deque

# 스타트 링크 빌딩의 층수, 성호의 위치, 스타트링크 사무실의 층, U 이동층 수, D 이동층 수
F, S, G, U, D = map(int, input().split())

buidings = [0] * (F + 1)
buidings[S] = 1

q = deque([S])

while q:
    cur = q.popleft()
    for next in [cur + U, cur - D]:
        if 0 < next <= F:
            if buidings[next] == 0:
                buidings[next] = buidings[cur] + 1
                q.append(next)
                    

print(buidings[G] - 1 if buidings[G] != 0 else "use the stairs")