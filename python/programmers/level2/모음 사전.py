cnt = 0
result = -1
flag = False
def dfs(c, compare, l=0):
    global cnt, result, flag
    if c == compare:
        flag = True
        result = cnt
        return
    if l == 5:
        return
    for t in ["A", "E", "I", "O", "U"]:
        cnt += 1
        dfs(c + t, compare, l+1)
        if flag:    return


def solution(word):
    dfs("", word)
    return result

print(solution("AAAE"))