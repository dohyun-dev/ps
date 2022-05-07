#solve time 12
# level 2

from collections import defaultdict

def calc_score(choice):
    return 4 - choice if choice < 4 else choice - 4

def solution(survey, choices):
    answer = ""
    type_dict = defaultdict(int)
    
    for i in range(len(survey)):
        a, b = survey[i], choices[i]
        score = calc_score(b)
        if b < 4:
            type_dict[a[0]] += score
        else:
            type_dict[a[1]] += score
    
    for t1, t2 in [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]:
        if type_dict[t1] > type_dict[t2]:
            answer += t1
        elif type_dict[t1] < type_dict[t2]:
            answer += t2
        else:
            answer += chr(min(ord(t1), ord(t2)))
    
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))