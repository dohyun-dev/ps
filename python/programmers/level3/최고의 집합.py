def solution(n, s):
    answer, mod = [s // n] * n, s % n
    idx = n - 1

    if answer[0] == 0:
        return [-1]

    while mod != 0:
        answer[idx] += 1
        mod, idx = mod - 1, idx - 1
        if idx == -1:
            idx = n - 1
    return answer