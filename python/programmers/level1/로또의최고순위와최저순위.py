def generate_rank(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6
    

def solution(lottos, win_nums):
    check = set(win_nums)
    count = [0, 0]
    zero_cnt = 0
    for num in lottos:
        if num in check:
            count[0] += 1
            count[1] += 1
        if num == 0:
            count[0] += 1
    return sorted(generate_rank(cnt) for cnt in count)