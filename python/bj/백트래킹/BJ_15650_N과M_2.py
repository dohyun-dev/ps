import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, start=1):
    if l == M:
        print(" ".join([str(i) for i in range(1, N+1) if check[i]]), end="\n")
        return
    for i in range(start, N+1):
        if not check[i]:
            check[i] = True
            DFS(l+1, i+1)
            check[i] = False

N, M = map(int, input().split())
check = [False] * (N + 1)
DFS()