def dfs(word, target):
    global answer

    if target == word:
        answer = 1
        return
    if len(target) == 0:
        return

    if target[-1] == "A":
        dfs(word, target[:-1])
    if target[0] == "B":
        dfs(word, target[1:][::-1])

answer = 0
dfs(input(), input())
print(answer)