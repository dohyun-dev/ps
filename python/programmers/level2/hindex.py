def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        h = len(citations) - i
        if h <= citations[i]:
            return h
    return 0