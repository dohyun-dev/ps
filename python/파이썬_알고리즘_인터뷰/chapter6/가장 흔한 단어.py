import re
from collections import Counter


def solution(paragraph: str, banned:list):
    result = []
    for word in re.sub('[^\w]', ' ', paragraph).split():
        if word not in banned:
            result.append(word)
    return Counter(result).most_common(1)[0][0]


# def solution(paragraph: str, banned:list):
#     counter = defaultdict(int)
#     for word in re.sub('[^\w]', ' ', paragraph).split():
#         if word not in banned:
#             counter[word] += 1
#     return max(counter, key=counter.get)



print(solution("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
