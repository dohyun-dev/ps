from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for permu in permutations(dungeons):
        cur_stamina, cnt = k, 0
        for dungeons in permu:
            if cur_stamina >= dungeons[0]:
                cur_stamina -= dungeons[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))