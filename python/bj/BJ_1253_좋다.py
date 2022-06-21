import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
check = defaultdict(list)

for i in range(N):
    for j in range(i+1, N):
        check[arr[i] + arr[j]].append((i, j))

answer = 0

for idx, num in enumerate(arr):
    if num in check:
        for a, b in check[num]:
            if idx != a and idx != b:
                answer += 1
                break
print(answer)