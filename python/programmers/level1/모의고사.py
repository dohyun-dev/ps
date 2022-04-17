def solution(answers):
    solve_case = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    answer = [0] * 4
    for i, case in enumerate(solve_case):
        for idx, a in enumerate(answers):
            if case[idx % len(case)] == a:
                answer[i+1] += 1
    max_result = max(answer)
    return [i for i in range(1, 4) if max_result == answer[i]]