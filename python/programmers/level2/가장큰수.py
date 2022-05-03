import functools 

def comparator(a, b):
    a, b = int(a + b), int(b + a)
    return 0 if a == b else (1 if a > b else -1)

def solution(numbers):
    return str(int("".join(sorted(map(str, numbers), key=functools.cmp_to_key(comparator),reverse=True))))