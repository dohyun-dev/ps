import sys; input = lambda : sys.stdin.readline().rstrip()

def check(arr, m):
    return sum([(arr[i+1] - arr[i]) // m - 1 if (arr[i+1] - arr[i]) % m == 0 else (arr[i+1] - arr[i]) // m for i in range(len(arr)-1) if arr[i+1] - arr[i] > m and arr[i+1] - arr[i] > 0])

N, M, L = map(int, input().split())
rest_area = [0] + sorted(list(map(int, input().split()))) + [L]
lt, rt = 1, L
answer = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(rest_area, mid) > M:
        lt = mid + 1
    else:
        answer = mid
        rt = mid - 1
print(answer)