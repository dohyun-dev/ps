N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 1)
M = 0
for i in range(N):
    M = max(M, dp[i])
    if i + arr[i][0] <= N:
        dp[i + arr[i][0]] = max(M + arr[i][1], dp[i + arr[i][0]])
print(max(dp))