import sys; input = lambda : sys.stdin.readline().rstrip()

for x in [int(input()) for _ in range(int(input()))]:
    dp = [(1, 0), (0, 1)]
    for i in range(2, x+1):
        dp.append((dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]))
    print(*dp[x])