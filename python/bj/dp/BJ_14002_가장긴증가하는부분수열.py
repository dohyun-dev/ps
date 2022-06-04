N = int(input())
arr = list(map(int, input().split()))
dp = [(1, [arr[i]]) for i in range(N)]
for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and dp[i][0] < dp[j][0] + 1:
            dp[i] = (dp[j][0] + 1, dp[j][1] + [arr[i]])
result = max(dp)
print(result[0])
print(*result[1])