import sys; input = lambda : sys.stdin.readline().rstrip()

N, S = map(int, input().split())
arr = [*map(int, input().split())]

st, end = 0, 0
sum_value = 0
answer = sys.maxsize

while True:
    if sum_value >= S:
        answer = min(answer, end - st)
        sum_value -= arr[st]
        st += 1
    elif end == N:
        break
    else:
        sum_value += arr[end]
        end += 1

print(answer if answer != sys.maxsize else 0)