from itertools import combinations_with_replacement

def solution(n, info):
    result = [-1]
    max_gap = -1

    for combi in combinations_with_replacement(range(10, -1, -1), n):
        lion = [0] * 11

        for i in combi:
            lion[i] += 1

        apeach_score, lion_score = 0, 0

        for i in range(0, 11):
            if info[i] == 0 and lion[i] == 0:
                continue
            if info[i] < lion[i]:
                lion_score += 10 - i
            else:
                apeach_score += 10 - i

        if apeach_score < lion_score:
            if max_gap <= lion_score - apeach_score:
                max_gap = lion_score - apeach_score
                result = lion
        print(combi)
    return result

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))