from collections import Counter

def solution(N, stages):
    answer = [0] * (N + 2)
    for s in stages:
        for i in range(1, s+1):
            answer[i] += 1
    counter = Counter(stages)
    
    for i in range(1, N+1):
        if i in counter:
            answer[i] = counter[i] / answer[i]
        else:
            answer[i] = 0
    
    return sorted([i for i in range(1, N+1)], key= lambda x: -answer[x])