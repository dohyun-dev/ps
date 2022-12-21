import math


def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a
    while a != b:
        print(a, b)
        if a % 2 == 1 and a + 1 == b:
            break
        a, b = math.ceil(a / 2), math.ceil(b / 2)
        answer += 1
    return answer

print(solution(8, 4, 7))