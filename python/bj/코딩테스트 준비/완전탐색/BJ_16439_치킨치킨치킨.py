def calc_score(periods, select):
    return sum([max(period[i] for i in select) for period in periods])

def combi(l, select, pre):
    global answer
    if l == 3:
        answer = max(answer, calc_score(periods, select))
        return
    for i in range(pre, M):
        combi(l + 1, select + [i], i + 1)

N, M = map(int, input().split())
periods = [[*map(int, input().split())] for _ in range(N)]
answer = 0
combi(0, [], 0)
print(answer)
