from sys import prefix

N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)
result = []

for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
for _ in range(M):
    a, b = map(int, input().split())
    result.append(str(prefix_sum[b] - prefix_sum[a-1]))

print(prefix_sum)

print("\n".join(result))