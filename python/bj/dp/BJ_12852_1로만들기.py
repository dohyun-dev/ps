import sys; input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0] * (N + 1)
pre = [[]] * (N + 1)
dp[1], pre[1] = 0, [1]

for x in range(2, N+1):
    dp[x] = dp[x-1] + 1
    pre[x] = [x] + pre[x-1]
    if x % 3 == 0 and dp[x // 3] + 1 < dp[x]:
        dp[x] = dp[x // 3] + 1
        pre[x] = [x] + pre[x // 3]
    if x % 2 == 0 and dp[x // 2] + 1 < dp[x]:
        dp[x] = dp[x // 2] + 1
        pre[x] = [x] + pre[x // 2]

print(dp[N])
print(*pre[N])