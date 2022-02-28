import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [10001] * (K + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, K+1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[K] if dp[K] != 10001 else -1)