import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, result=[], num_set=set(), start=0):
    if l == M:
        p = " ".join(result)
        if p not in num_set:
            print(p)
            num_set.add(p)
        return
    for i in range(start, N):
        result.append(nums[i])
        DFS(l+1, result, num_set, i)
        result.pop()
        
N, M = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
DFS()