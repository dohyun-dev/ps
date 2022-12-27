import re

def dfs(cur, n, check, banned, answer):
    if cur == n:
        if len(check) == n:
            answer.add("".join(sorted(check)))
        return
    else:
        for ban in banned[cur]:
            if ban in check:
                continue
            check.add(ban)
            dfs(cur + 1, n, check, banned, answer)
            check.remove(ban)

def solution(user_id, banned_id):
    banned, answer = [], set()
    for word in banned_id:
        word = word.replace("*", ".")
        banned.append([user for user in user_id if re.fullmatch(word, user)])
    dfs(0, len(banned), set(), banned, answer)
    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))