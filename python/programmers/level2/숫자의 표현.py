def solution(n):
    answer = 0
    cur_value, left = 0, 0
    for right in range(1, n + 1):
        cur_value += right

        while cur_value > n:
            cur_value -= left
            left += 1

        if cur_value == n:
            answer += 1
    return answer