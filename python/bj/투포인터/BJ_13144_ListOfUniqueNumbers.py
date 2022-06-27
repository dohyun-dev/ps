import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [*map(int, input().split())]

st, end = 0, 1
temp = set()
temp.add(arr[0])

while end <= N:
    if len(temp) == end - st:
        answer += 1
        end += 1
        try:
            temp.add(arr[end])
        except:
            break
    else:

