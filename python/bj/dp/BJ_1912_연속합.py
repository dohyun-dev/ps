N = int(input())
dp = [0]
for cur in map(int, input().split()):   dp.append(max(cur, dp[-1] + cur))
print(max(dp[1:]))