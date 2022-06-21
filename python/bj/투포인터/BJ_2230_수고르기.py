import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
st, ed = 0, 1
result = sys.maxsize
arr.sort()

while st < N and ed < N:
    tmp = arr[ed] - arr[st]
    if tmp < M:
        ed += 1
    else:
        result = min(result, tmp)
        st += 1
print(result)