def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t >= 1:
        t = c % d
        c, d = d, t
    return [c, int(a * b / c)]

def solution(n, m):
    return gcdlcm(n, m)