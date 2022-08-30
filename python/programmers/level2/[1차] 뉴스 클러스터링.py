from collections import Counter
import math

def cut_word(str):
    return Counter([str[i:i+2].lower() for i in range(len(str) - 1) if str[i:i+2].isalpha()])

def J(set1, set2):
    if not len(set1.values()) and not len(set2.values()):
        return 65536
    intersection, union = 0, 0

    for k, v in [*set1.items()] + [*set2.items()]:
        union += v

    for k, v in set1.items():
        if k in set2:
            intersection += min(v, set2[k])

    return math.floor(intersection / (union - intersection) * 65536)

def solution(str1, str2):
    set1 = cut_word(str1)
    set2 = cut_word(str2)
    return J(set1, set2)

print(solution("aa1+aa2", "AAAA12"))