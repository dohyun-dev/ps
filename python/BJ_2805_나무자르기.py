import sys; input = lambda : sys.stdin.readline().rstrip()

def check(arr, target):
    return sum(x - target for x in arr if x - target > 0)

N, M = map(int, input().split())
trees = list(map(int, input().split()))
lt, rt = 1, max(trees)
result = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if check(trees, mid) >= M:
        result = mid        
        lt = mid + 1
    else:
        rt = mid - 1
        
print(result)