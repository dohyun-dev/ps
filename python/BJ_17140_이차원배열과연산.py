import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import Counter

r, c, k = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    a = list(map(int, input().split()))
    for j in range(3):
        arr[i][j] = a[j]

def row_process():
    global arr, r
    temp = [[] for _ in range(100)]
    for i in range(r):
        for a, b in sorted(Counter([x for x in arr[i] if arr[i] != 0]).most_common(), key=lambda x: (x[1], x[0])):
            temp[i].append(a)
            temp[i].append(b)
    
    r = max(map(lambda x : len(x), temp))
    
    for a in temp:
        for _ in range(r - len(a)):
            a.append(0)
    
    arr = temp
    print(arr)
    if r < c:
        arr = list(zip(*arr))
    print(arr)
    
    
for cnt in range(1, 102):
    if arr[r][c] == k:
        print(cnt)
        break
    if cnt <= 101:
        row_process()
print(-1)