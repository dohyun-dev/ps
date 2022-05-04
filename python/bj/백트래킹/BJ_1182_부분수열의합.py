import sys; input = lambda : sys.stdin.readline().rstrip()


def dfs(l=0, s=0, cnt=0):
    global answer
    if l == N:
        if cnt != 0 and s == S:
            answer += 1
        return
    dfs(l+1, s + arr[l], cnt+1)
    dfs(l+1, s, cnt)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
dfs()
print(answer)