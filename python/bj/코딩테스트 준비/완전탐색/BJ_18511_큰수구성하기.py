import sys


def dfs(l=0, result=""):
    global answer
    result = int(result) if result else 0
    if result > N or l == limit_level + 1:
        return
    if result > answer:
        answer = result
        return

    for num in nums:
        dfs(l+1, num + str(result if result else ""))

N, K = map(int, input().split())
nums = [""] + input().split()
limit_level = len(str(N))
answer = 0

dfs()
print(answer)

