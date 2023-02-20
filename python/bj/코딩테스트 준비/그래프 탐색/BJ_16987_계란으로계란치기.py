from itertools import permutations

def dfs(l=0, cnt=0):
    global answer

    if l == N:
        answer = max(answer, cnt)
        return

    s1, w1 = eggs[l]

    if s1 <= 0:
        dfs(l+1, cnt)
        return

    flag = True
    for i in range(N):
        s2, w2 = eggs[i]
        if l == i or s2 <= 0:
            continue
        eggs[l], eggs[i] = (s1-w2, w1), (s2-w1, w2)
        if eggs[l][0] <= 0 and eggs[i][0] <= 0:
            dfs(l+1, cnt+2)
            flag = False
        elif eggs[l][0] <= 0 or eggs[i][0] <= 0:
            dfs(l+1, cnt+1)
            flag = False
        else:
            dfs(l+1, cnt)
            flag = False
        eggs[l], eggs[i] = (s1, w1), (s2, w2)
    if flag:
        dfs(l+1, cnt)

N = int(input())
eggs = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0
dfs()
print(answer)