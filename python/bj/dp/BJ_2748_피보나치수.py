N = int(input())
dp = [0, 1]
for _ in range(N+1):
    dp.append(dp[-1] + dp[-2])
print(dp[N])