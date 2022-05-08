import sys; input = lambda : sys.stdin.readline().rstrip()


def DFS(l=0, result=[], set_num=set()):
    if l == M:
        permu = " ".join(result)
        if permu not in set_num:
            print(permu)
            set_num.add(permu)
        return
    for i in range(N):
        if not check[i]:
            check[i] = True
            result.append(nums[i])
            DFS(l+1, result, set_num)
            result.pop()
            check[i] = False
        
N, M = map(int, input().split())
nums = sorted(input().split(), key=lambda x: int(x))
check = [False] * N
DFS()