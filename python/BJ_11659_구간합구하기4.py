from sys import prefix


N, M = map(int, input().split())

arr = list(map(int, input().split()))
prefix_sum = [0]
result = []

for i in range(N):
    prefix_sum.append(prefix_sum[-1] + arr[i])
    
for _ in range(M):
    a, b = map(int, input().split())
    result.append(str(prefix_sum[b] - prefix_sum[a-1]))

print("\n".join(result))