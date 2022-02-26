N, M = map(int, input().split())
arr = list(map(int, input().split()))
end, summary = 0, 0
cnt = 0

for start in range(N):
    while summary < M and end < N:
        summary += arr[end]
        end += 1
    if summary == M:
        cnt += 1
    summary -= arr[start]

print(cnt)