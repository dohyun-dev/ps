import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [[0] * (N + 1)]
for i in range(N):  arr.append([0] + list(map(int, input().split())))
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != 1 and j == 1:
            arr[i][j] += arr[i-1][N]
        else:
            arr[i][j] += arr[i][j-1]

result = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 != 1 and y1 == 1:
        x = x1 - 1
        y = N
    else:
        x = x1
        y = y1-1
        
    result.append(arr[x2][y2] - arr[x][y])
print("\n".join(map(str, result)))