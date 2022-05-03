score_gap = 0
result = [-1]

def max_result(info, temp):
    global result, score_gap
    ryan = [0] * 11
    
    for i in temp:
        ryan[i] += 1
    
    peach_score, ryan_score = 0, 0
    for i in range(1, 11):
        if info[i] != 0 and ryan[i] == 0:
            peach_score += i
        elif info[i] == 0 and ryan[i] != 0:
            ryan_score += i
        elif info[i] != 0 and ryan[i] != 0:
            if info[i] >= ryan[i]:
                peach_score += i
            else:
                ryan_score += i
    if peach_score < ryan_score:
        if len(result) == 1:
            score_gap = ryan_score - peach_score
            result = ryan
        elif score_gap < ryan_score - peach_score:
            score_gap = ryan_score - peach_score
            result = ryan
        elif score_gap == ryan_score - peach_score:
            for i in range(11):
                if result[i] > ryan[i]:
                    return True
                elif result[i] < ryan[i]:
                    result = ryan
                    break
    return False

ryan_arrow = []
flag = False
def dfs(N, info, pre=10, l=0):
    global flag
    if l == N:
        flag = max_result(info, ryan_arrow)
        return
    for i in range(pre, -1, -1):
        ryan_arrow.append(i)
        dfs(N, info, pre, l+1)
        ryan_arrow.pop()
        if flag:    return
                    
def solution(n, info):
    info = info[::-1]
    dfs(n, info, 10)
    return result[::-1]

print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))