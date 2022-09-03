def convert(n, k):
    result = ""
    while n:
        result = str(n % k) + result
        n //= k
    return result.split("0")

def is_primary(value):
    if value < 2:
        return False

    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

def solution(n, k):
    words = convert(n, k)
    cnt = 0
    for word in words:
        if word != "" and is_primary(int(word)):
            cnt += 1
    return cnt