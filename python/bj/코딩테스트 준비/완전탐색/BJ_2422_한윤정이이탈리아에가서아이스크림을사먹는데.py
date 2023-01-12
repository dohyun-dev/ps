N, M = map(int, input().split())
no_combi = {i: set() for i in range(1, N+1)}
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    no_combi[a].add(b)
    no_combi[b].add(a)

for i in range(1, N+1):
    for j in range(i+1, N+1):
        if j in no_combi[i]:
            continue
        for k in range(j+1, N+1):
            if k in no_combi[j] or k in no_combi[i]:
                continue
            answer += 1
print(answer)