def solution(n):
    answer = [True] * (n + 1)
    
    for i in range(2, n + 1):
        if not answer[i]:   continue
        for j in range(i+i, n+1, i):
                answer[j] = False
            
    return sum(map(lambda x: 1 if x == True else 0 ,answer[2 : n + 1]))

def solution2(n):
    primary_num = set(range(2, n+1))
    
    for i in range(2, n+1):
        if i in primary_num:
            primary_num -= set(range(i+i, n+1, i))