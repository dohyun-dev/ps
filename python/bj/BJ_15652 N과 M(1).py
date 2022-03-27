result = []
def DFS(check, l=0):
    if l == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(1, N+1):
            if check[i]: continue
            check[i] = True
            result.append(i)
            DFS(check, l+1)
            result.pop()   
            check[i] = False      

N, M = map(int, input().split())
check = [False for i in range(N+1)]
DFS(check)