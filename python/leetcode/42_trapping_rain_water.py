import sys; input = lambda : sys.stdin.readline().rstrip()

map(int, input().split())
arr = list(map(int, input().split()))
answer, lt, rt = 0, 0, len(arr) - 1
max_rain = max(arr)
left_max, right_max = 0, 0

while lt <= rt:
    if left_max <= right_max:
        if left_max <= arr[lt]:
            left_max = arr[lt]
        else:
            answer += left_max - arr[lt]
        lt += 1
    else:
        if right_max <= arr[rt]:
            right_max = arr[rt]
        else:
            answer += right_max - arr[rt]
        rt -= 1

print(answer)