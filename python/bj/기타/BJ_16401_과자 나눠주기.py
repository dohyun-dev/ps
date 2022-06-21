import sys; input = lambda : sys.stdin.readline().rstrip()

def check(arr, target):
    return sum(x // target for x in arr)

M, N = map(int, input().split())
snacks = list(map(int, input().split()))
lt, rt = 1, max(snacks)
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(snacks, mid) >= M:
        result = mid        
        lt = mid + 1
    else:
        rt = mid - 1
print(result)