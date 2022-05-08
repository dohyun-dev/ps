import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, result=[], start=0):
    if l == M:
        print(" ".join(result), end="\n")
        return
    for i in range(start, N):
        result.append(nums[i])
        DFS(l+1, result, i)
        result.pop()
        
N, M = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
DFS()