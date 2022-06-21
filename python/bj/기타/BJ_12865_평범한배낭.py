import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0]) 
dp = [[0] * (K + 1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = arr[i-1]
    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])