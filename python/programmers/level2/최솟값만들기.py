from functools import reduce
def solution(A,B):
    A.sort();   B.sort(reverse=True)
    return reduce(lambda acc, cur: acc + (cur[0] * cur[1]), zip(A, B), 0)
    
    