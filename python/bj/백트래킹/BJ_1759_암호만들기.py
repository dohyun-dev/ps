import sys; input = lambda : sys.stdin.readline().rstrip()

def combinations(l=0, start=0, result=[]):
    if l == L:
        모음, 자음 = 0, 0
        for c in result:
            if c in "aeiou":
                모음 += 1
            else:
                자음 += 1
        if 모음 >= 1 and 자음 >= 2:
            print("".join(result))
        return
    for i in range(start, C):
        result.append(char_arr[i])
        combinations(l+1, i+1, result)
        result.pop()
        
L, C = map(int, input().split())
char_arr = sorted(input().split())
combinations()