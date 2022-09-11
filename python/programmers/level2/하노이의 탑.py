def hanoi(n, a, b, c, result):
    if n == 1:
        result.append([a, c])
    else:
        hanoi(n - 1, a, c, b, result)
        result.append([a, c])
        hanoi(n - 1, b, a, c, result)


def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer