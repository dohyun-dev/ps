result = []
def DFS(l=0):
    if l >= 2 and result[-1] < result[-2]:
        return
    if l == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(1, N+1):
            if not check[i]:
                check[i] = True
                result.append(i)     
                DFS(l+1)
                result.pop()
                check[i] = False
                

N, M = map(int, input().split())
check = [False for i in range(N+1)]
DFS()