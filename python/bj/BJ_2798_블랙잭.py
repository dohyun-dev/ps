import sys; input = lambda : sys.stdin.readline().rstrip()
    

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = -float("inf")

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            temp = arr[i] + arr[j] + arr[k]
            if temp <= M and result < temp:
                result = temp
print(result)
    