import sys; input = lambda : sys.stdin.readline().rstrip()

n = int(input())
dp = [sys.maxsize for _ in range(n+1)]
dp[0] = 0
dp[1] = 0

for i in range(2, n+1):
    if i % 2 == 0:  dp[i] = min(dp[i//2] + 1, dp[i])
    if i % 3 == 0:  dp[i] = min(dp[i//3] + 1, dp[i])
    dp[i] = min(dp[i-1] + 1, dp[i])

print(dp[n])