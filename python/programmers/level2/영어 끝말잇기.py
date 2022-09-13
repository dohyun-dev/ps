def solution(n, words):
    check = set([words[0]])
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or words[i] in check:
            return [i%n+1, i//n+1]
        check.add(words[i])
    return [0, 0]