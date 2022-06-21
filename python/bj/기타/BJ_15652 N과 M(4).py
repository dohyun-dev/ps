result = []
def DFS(l=0):
    if l == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(1, N+1):
            result.append(i)
            DFS(l+1)
            result.pop()         

N, M = map(int, input().split())
DFS()