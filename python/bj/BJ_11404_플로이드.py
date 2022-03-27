import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = int(input()), int(input())
dp = [[sys.maxsize] * N for _ in range(N)]

for i in range(M):
    s, e, cost = map(int, input().split())
    dp[s-1][e-1] = min(dp[s-1][e-1], cost)

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i != j:
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for x in dp:
    print(" ".join(map(lambda x : str(x) if x != sys.maxsize else "0", x)))