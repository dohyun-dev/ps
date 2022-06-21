import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0] * (K + 1)
dp[0] = 1

for coin in coins:
    for i in range(1, K+1):
        if i - coin >= 0:
            dp[i] += dp[i - coin]

print(dp[K])