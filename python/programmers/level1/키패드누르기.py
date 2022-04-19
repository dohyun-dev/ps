location = {
    1: (0, 0), 4: (1, 0), 7: (2, 0), -1: (3, 0), 
    2: (0, 1), 5: (1, 1), 8: (2, 1), 0: (3, 1), 
    3: (0, 2), 6: (1, 2), 9: (2, 2), -2: (3, 2)}
left = {1, 4, 7, -1}
right = {3, 6, 9, -2}


def solution(numbers, hand):
    result = ""
    left_thumb, right_thumb = -1, -2    # 손가락 현재 위치
    
    for n in numbers:
        flag = 0 # 왼손 1 오른손 2
        if n in left:
            flag = 1
        elif n in right:
            flag = 2
        else:
            left_temp = abs(location[n][0] - location[left_thumb][0]) + abs(location[n][1] - location[left_thumb][1])
            right_temp = abs(location[n][0] - location[right_thumb][0]) + abs(location[n][1] - location[right_thumb][1])
            if left_temp < right_temp:
                flag = 1
            elif left_temp > right_temp:
                flag = 2
            else:
                if hand == 'left':
                    flag = 1
                else:
                    flag = 2
        if flag == 1:
            left_thumb = n
            result += "L"
        else:
            right_thumb = n
            result += "R"
    
    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))