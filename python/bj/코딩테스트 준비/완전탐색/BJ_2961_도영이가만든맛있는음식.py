def dfs(l, cnt, s, b):
    global answer
    if l == N:
        if cnt != 0:
            answer = min(answer, abs(s - b))
        return
    dfs(l + 1, cnt + 1, s * materials[l][0], b + materials[l][1])
    dfs(l + 1, cnt, s, b)

N = int(input())
materials = [tuple(map(int, input().split())) for _ in range(N)]
answer = float("inf")
dfs(0, 0, 1, 0)
print(answer)