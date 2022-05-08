def convert_binary(s):
    answer = ""
    while s != 0:
        answer = str(s % 2) + answer
        s //= 2
    return answer

def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[0] += 1
        temp = len(s)
        s = s.replace("0", "")
        temp -= len(s)
        answer[1] += temp
        s = convert_binary(len(s))
        
    return answer