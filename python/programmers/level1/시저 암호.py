def solution(s, n):
    result = ""
    a, z = ord('a'), ord('z')
    A, Z = ord('A'), ord('Z')
    
    for c in s:
        if c.isalpha():
            new_num = ord(c) + n
            if a <= ord(c) <= z:
                if new_num > z:
                    result += chr(new_num % z + a - 1)
                else:
                    result += chr(new_num)
            elif A <= ord(c) <= Z:
                if new_num > Z:
                    result += chr(new_num % Z + A - 1)
                else:
                    result += chr(new_num)
        else:
            result += c
    return result