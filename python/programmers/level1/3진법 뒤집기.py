def convert(n):
    result = ""
    while n > 0:
        result = result + str(n % 3)
        n //= 3
    return result

def solution(n):
    answer = 0
    return int(convert(n), 3)