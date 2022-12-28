def return_num(num):
    if num == 1:
        return 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return num // i
    else:
        return 1

def solution(begin, end):
    answer = [0] * (end - begin + 1)
    for i in range(len(answer)):
        answer[i] = return_num(i + begin)
    return answer

print(solution(1, 10))