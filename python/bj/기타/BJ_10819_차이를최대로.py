import sys; input = lambda : sys.stdin.readline().rstrip();
def permutations(l):
    global res
    if l == n:
        res = max(res, calc(numset))
        return
    for i in range(n):
        if not vist[i]:
            vist[i] = True
            numset[l] = arr[i]
            permutations(l+1)
            vist[i] = False
            
def calc(arr):
    temp = 0
    for i in range(1, n):
        temp += abs(arr[i-1] - arr[i])
    return temp

n, arr = int(input()), list(map(int, input().split()))
vist = [False] * n
numset = [0] * n
res = -float("inf")
permutations(0)
print(res)

