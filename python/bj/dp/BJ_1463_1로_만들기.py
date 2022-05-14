import sys; input = lambda : sys.stdin.readline().rstrip()

x = int(input())
dp = [sys.maxsize] * (x + 1)
dp[1] = 0
for i in range(2, x+1):
    dp[i] = dp[i - 1] + 1
    if not i % 2:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if not i % 3:
        dp[i] = min(dp[i // 3] + 1, dp[i])
print(dp[x])