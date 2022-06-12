import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(N+1)]
dp = [[0] * (M + 1) for _ in range(N+1)]

for i in range(N):
    for idx, j in enumerate(list(map(int, input()))):
        arr[i+1][idx+1] = j

for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j]:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1

print(max(max(i) for i in dp) ** 2)