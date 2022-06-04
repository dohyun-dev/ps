import sys; input = lambda : sys.stdin.readline().rstrip()

dp = [0] * 101
dp[0], dp[1], dp[2] = 0, 1, 1
result = []
for _ in range(int(input())):
    n = int(input())
    for i in range(2, n+1):
        if not dp[i]:
            dp[i] = dp[i-2] + dp[i-3]
    result.append(str(dp[n]))
print("\n".join(result))