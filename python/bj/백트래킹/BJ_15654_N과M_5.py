import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, result=[]):
    if l == M:
        print(" ".join(result), end="\n")
        return
    for i in range(N):
        if check[i]:    continue
        check[i] = True
        result.append(nums[i])
        DFS(l+1, result)
        result.pop()
        check[i] = False
        
N, M = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
check = [False] * N
DFS()