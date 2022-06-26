import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import Counter

N, K = map(int, input().split())
arr = [*map(int, input().split())]
answer = 0
counter = [0] * (max(arr) + 1)
st, end = 0, 0
while end < len(arr):
    if counter[arr[end]] < K:
        counter[arr[end]] += 1
        end += 1
        answer = max(answer, end - st)
    else:
        counter[arr[st]] -= 1
        st += 1
print(answer)