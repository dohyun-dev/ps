import sys; input = lambda : sys.stdin.readline().rstrip()

D, N = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(D-1):
    if oven[i] < oven[i+1]: 
        oven[i+1] = oven[i]

lt, rt = 0, D - 1
for p in pizza:
    flag = True
    flag2 = True
    while lt <= rt:
        mid = (lt + rt) // 2
        if oven[mid] >= p:
            result = mid
            lt = mid + 1
            flag = False
        else:
            flag2 = False
            rt = mid - 1
    if flag:
        print(0)
        exit()
    if not flag and flag2:  rt = result - 1
        
    lt = 0
    
print(rt)