def solution(n):
    for x in range(1, int(n ** 0.5) + 1):
        if x ** 2 == n:
            return (x + 1) ** 2
    return -1