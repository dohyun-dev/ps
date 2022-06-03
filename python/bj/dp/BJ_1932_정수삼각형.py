import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [(list(map(int, input().split())) + ([-1] * N))[:N] for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = arr[0][0]

# 테두리 부분 초기화
for i in range(1, N):
    dp[i][0] = dp[i-1][0] + arr[i][0]
    dp[i][i] = dp[i-1][i-1] + arr[i][i]

for i in range(2, N):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + arr[i][j]
print(max(max(dp)))