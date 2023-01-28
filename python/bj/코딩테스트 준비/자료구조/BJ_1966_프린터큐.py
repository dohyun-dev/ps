from collections import deque

result = []
for _ in range(int(input())):
    N, M = map(int, input().split())
    q = deque((num, idx) for idx, num in enumerate(map(int, input().split())))
    max_num, cnt = max(q, key=lambda x: x[0])[0], 1
    while q:
        if q[0][0] == max_num:
            cur, idx = q.popleft()
            if idx == M:
                break
            max_num = max(q, key=lambda x: x[0])[0]
            cnt += 1
        else:
            q.rotate(-1)
    result.append(f'{cnt}')
print("\n".join(result))
