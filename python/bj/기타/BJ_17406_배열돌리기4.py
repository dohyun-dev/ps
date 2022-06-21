import sys; input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations
from copy import deepcopy

def min_arr_value(arr):
    return min(sum(a) for a in arr)

def copy_array_range(r1, r2, c1, c2, arr):
    temp_arr = []
    for i in range(r1, r2 + 1):
        temp = []
        for j in range(c1, c2 + 1):
            temp.append(arr[i][j])
        temp_arr.append(temp)
    return temp_arr

def reflect_change_arr(r1, r2, c1, c2, temp_arr, arr):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            arr[i][j] = temp_arr[i-r1][j-c1]

def solution(r, c, s, arr):
    r1, c1, r2, c2 = r - s - 1, c - s - 1, r + s - 1, c + s - 1
    temp_arr = copy_array_range(r1, r2, c1, c2, arr)
    N, M = len(temp_arr), len(temp_arr[0])
    K = min(N, M) // 2

    for k in range(K):
        first_result = temp_arr[k][k]
        for i in range(k, N-k-1):
            temp_arr[i][k] = temp_arr[i+1][k]
        for j in range(k, M-k-1):
            temp_arr[N-k-1][j] = temp_arr[N-k-1][j+1]
        for i in range(N-k-1, k, -1):
            temp_arr[i][M-k-1] = temp_arr[i-1][M-k-1]
        for j in range(M-k-1, k, -1):
            temp_arr[k][j] = temp_arr[k][j-1]
        temp_arr[k][k+1] = first_result
    reflect_change_arr(r1, r2, c1, c2, temp_arr, arr)

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
query = [tuple(map(int, input().split())) for _ in range(K)]
answer = sys.maxsize

for p in permutations(query):
    copy_arr = deepcopy(arr)
    for q in p:
        r, c, s = q
        solution(r, c, s, copy_arr)
    answer = min(answer, min_arr_value(copy_arr))
print(answer)