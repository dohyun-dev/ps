import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M + 1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + arr[i-1][j-1]

for _ in range(int(input())):
    r1, c1, r2, c2 = map(int, input().split())
    print(dp[r2][c2] - (dp[r1-1][c2] + dp[r2][c1-1] - dp[r1-1][c1-1]))