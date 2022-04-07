def solution(x):
    origin = x
    tmp = 0
    while origin != 0:
        tmp += origin % 10
        origin //= 10
    return x % tmp == 0