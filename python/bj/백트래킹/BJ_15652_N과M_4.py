import sys; input = lambda : sys.stdin.readline().rstrip()

def DFS(l=0, start=1):
    if l == M:
        print(" ".join(result), end="\n")
        return
    for i in range(start, N+1):
        result.append(str(i))
        DFS(l+1, i)
        result.pop()
N, M = map(int, input().split())
result = []
DFS()