from bisect import bisect_left
import sys; input = lambda: sys.stdin.readline().rstrip()

N, arr1 = int(input()), list(sorted(map(int, input().split())))
M, arr2 = int(input()), list(map(int, input().split()))
for num in arr2:
    if 0 <= (x:= bisect_left(arr1, num)) < len(arr1) and arr1[x] == num:
        print(1)
    else:
        print(0)