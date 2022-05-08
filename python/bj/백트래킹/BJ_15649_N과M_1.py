import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, result:str =""):
    if l == M:
        print(result.lstrip())
        return
    for i in range(1, N+1):
        if not check[i]:
            check[i] = True
            DFS(l+1, result + " " + str(i))
            check[i] = False

N, M = map(int, input().split())
check = [False for i in range(N+1)] 
DFS()