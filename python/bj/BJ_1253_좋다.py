import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(sorted(map(int, input().split())))
answer = 0

for i in range(N):
    temp = arr[:i] + arr[i+1:]
    st, en = 0, len(temp) -1
    while st < en:
        sum = temp[st] + temp[en]
        if arr[i] == sum:
            answer += 1
            break
        elif arr[i] > sum:
            st += 1
        else:
            en -= 1
print(answer)