from collections import Counter, deque, defaultdict

def solution(k, tangerine):
    answer = 0
    counter = defaultdict(list)
    for t in tangerine:
        counter[t].append(1)
    for size, count in Counter(tangerine).most_common():
        if k <= 0:
            break
        answer += 1
        k -= count
    return answer