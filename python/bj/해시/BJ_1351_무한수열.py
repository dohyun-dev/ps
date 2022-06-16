def DFS(i):
    if i < 1:
        return 1
    elif i in A:
        return A[i]
    A[i] = DFS(i // P) + DFS(i // Q)
    return A[i]

N, P, Q = map(int, input().split())
A = {}
print(DFS(N))