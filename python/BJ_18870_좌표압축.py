import sys; input = lambda : sys.stdin.readline().rstrip()
from bisect import bisect_left

N, arr = int(input()), list(map(int, input().split()))
sorted_arr = sorted(list(set(arr)))
print(" ".join(str(bisect_left(sorted_arr, x)) for x in arr))