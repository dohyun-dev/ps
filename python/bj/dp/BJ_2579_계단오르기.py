N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(2)]
dp[0][1], dp[1][1] = arr[1], arr[1]
for i in range(2, N+1):
    dp[0][i] = dp[1][i-1] + arr[i]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + arr[i]
print(max(dp[0][-1], dp[1][-1]))