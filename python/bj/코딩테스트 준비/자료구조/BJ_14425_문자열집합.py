N, M = map(int, input().split())
arr_set = set(input() for _ in range(N))
answer = 0

for _ in range(M):
    if input() in arr_set:
        answer += 1

print(answer)