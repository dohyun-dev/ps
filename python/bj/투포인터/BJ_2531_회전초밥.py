import sys; input = lambda : sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)] * 2

end = 0
temp = []
answer = 0
for st in range(len(arr)):
    while end < len(arr) and end - st < k:
        temp.append(arr[end])
        end += 1
    cur = set(temp)
    if c not in cur:
        answer = max(answer, len(cur) + 1)
    else:
        answer = max(answer, len(cur))
    temp = temp[1:]
print(answer)