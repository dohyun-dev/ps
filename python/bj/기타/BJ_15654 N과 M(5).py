def DFS(l=0):
    if l == M:
        print(" ".join(map(str, result)))
    else:
        for i in range(N):
            if not check[i]:
                result[l] = num_set[i]
                check[i] = True
                DFS(l+1)
                check[i] = False

N, M = map(int, input().split())
num_set = sorted(list(map(int, input().split())))
result = [0] * M
check = [False] * N
DFS()