import re

def solution(dartResult):
    answer = [0] * 3
    pow_dict = {'S': 1, 'D': 2, "T": 3}
    for idx, p in enumerate(re.findall("(\d+)([SDT]{1})([*#]?)", dartResult)):
        score, pow_num, bonus = p
        answer[idx] = int(score) ** pow_dict[pow_num]
        
        if bonus == '*':
            if idx == 0:
                answer[idx] *= 2
            else:
                for i in range(idx-1, idx+1):
                    answer[i] *= 2
        elif bonus == '#':
            answer[idx] = -answer[idx]
    return sum(answer)
        
print(solution('"1D2S3T*"'))