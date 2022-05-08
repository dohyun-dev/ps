from collections import deque

def solution(q1, q2):
    answer = 0
    q1, q2 = deque(q1), deque(q2)
    sum_q1, sum_q2 = sum(q1), sum(q2)
    total = sum_q1 + sum_q2
    
    while sum_q1 != sum_q2:
        if answer > (len(q1) + len(q2)) * 2:
            return -1
        while q1 and sum_q1 > total // 2:
            if len(q1) == 1 and q[0] > total // 2:
                return -1
            sum_q1 -= q1[0]
            sum_q2 += q1[0]
            q2.append(q1.popleft())
            answer += 1
        while q2 and sum_q2 > total // 2:
            if len(q2) == 1 and q2[0] > total // 2:
                return -1
            sum_q2 -= q2[0]
            sum_q1 += q2[0]
            q1.append(q2.popleft())
            answer += 1
    return answer
    
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))