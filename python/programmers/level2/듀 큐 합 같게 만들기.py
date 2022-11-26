from collections import deque

def solution(queue1, queue2):
    arr = (queue1 + queue2) * 2
    total, left_total = sum(queue1 + queue2), sum(queue1)
    left, right, answer = 0, len(queue1), 0
    while left <= right and left < len(arr) and right < len(arr):
        right_total = total - left_total
        if left_total == right_total:
            return answer
        else:
            if left_total > right_total or right_total == 0:
                left_total -= arr[left]
                left += 1
            else:
                left_total += arr[right]
                right += 1
        answer += 1
    return -1