import functools 
def comparator(a, b):
    a, b = int(a + b), int(b + a)
    return 0 if a == b else (1 if a > b else -1)
n = int(input())
print(str(int("".join(sorted(input().split(), key=functools.cmp_to_key(comparator),reverse=True)))))