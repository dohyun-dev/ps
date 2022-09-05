from collections import defaultdict
from itertools import combinations

def solution(relation):
    row_len, col_len = len(relation), len(relation[0])
    candidates = []

    # 전체조합 구하기
    for i in range(1, row_len + 1):
        candidates.extend(combinations(range(col_len), i))

    # 유일성
    unique = []
    for candi in candidates:
        tmp = [tuple([row[i] for i in candi]) for row in relation]
        if len(set(tmp)) == row_len:
            unique.append(candi)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
