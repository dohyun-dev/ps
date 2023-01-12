from collections import Counter

N, M = map(int, input().split())
dnas = [input() for _ in range(N)]
answer = [Counter() for _ in range(M)]

for i in range(N):
    for j in range(M):
        answer[j][dnas[i][j]] += 1

answer = "".join(map(lambda x: sorted(x.most_common(), key=lambda x: (-x[1], x[0]))[0][0], answer))
cnt = 0

for i in range(N):
    for j in range(M):
        if answer[j] != dnas[i][j]:
            cnt += 1

print(answer, cnt, sep="\n")