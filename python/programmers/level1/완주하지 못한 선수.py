from collections import defaultdict

def solution(participant, completion):
    d = defaultdict(int)
    for p in participant:
        d[p] += 1
    for c in completion:
        d[c] -= 1
        if d[c] == 0:
            del d[c]
    return list(d.keys())[0]