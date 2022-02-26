import sys; input = lambda : sys.stdin.readline().rstrip()    

n = int(input())
result = []

def check(length):
    for i in range(1, length // 2 + 1):
        if result[-i:] == result[-2 * i: -i]: return True
    else:   return False

def permutation(l=0):
    if check(l):    return False
    if l == n:
        print("".join(result))
        return True;
    for i in ["1", "2", "3"]:
        result.append(i)
        if permutation(l+1): return True
        result.pop()
    return False

permutation()