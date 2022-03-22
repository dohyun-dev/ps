n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]
g = [0] * (n + 1)
h = [0] * (n + 1)
h[1] = stairs[1]
#f(x) = g(x-1) = h(x-2) + 1 

for i in range(2, n+1):
    g[i] = h[i-1] + stairs[i]
    h[i] = max(g[i-2], h[i-2]) + stairs[i]

print(max(g[n], h[n]))
