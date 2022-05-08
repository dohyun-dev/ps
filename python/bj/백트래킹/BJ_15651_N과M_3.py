import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0):
    if l == M:
        print(" ".join(result), end="\n")
        return
    for i in range(1, N+1):
        result.append(str(i))
        DFS(l+1)
        result.pop()
N, M = map(int, input().split())
result = []
DFS()