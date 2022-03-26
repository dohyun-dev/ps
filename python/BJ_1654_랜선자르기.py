import sys; input = lambda : sys.stdin.readline().rstrip()

def check(arr, cut):
    return sum([line // cut for line in arr])

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]
lt, rt = 1, max(lines)
answer = 0

while lt <= rt:
    mid = (lt + rt) // 2
    if N <= check(lines, mid):
        answer = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(answer)