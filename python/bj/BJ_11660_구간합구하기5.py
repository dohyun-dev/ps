import sys; input = lambda : sys.stdin.readline().rstrip()
from copy import deepcopy

N, M = map(int, input().split())
arr = [[0] * (N + 1)]
for i in range(N):  arr.append([0] +list(map(int, input().split())))

sum_number = [[0] * (N + 1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_number[i][j] = sum_number[i][j-1] + arr[i][j]
        
sum_number2 = deepcopy(sum_number)
        
for i in range(1, N+1):
    for j in range(1, N+1):
        sum_number2[i][j] = sum_number2[i-1][j] + sum_number[i][j]
    
result = []    
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result.append(str(sum_number2[x2][y2] - sum_number2[x1-1][y2] - sum_number2[x2][y1-1] + sum_number2[x1-1][y1-1]))
print("\n".join(result))
    