from collections import deque

def solution(priorities, location):
    q = deque(zip(priorities, range(len(priorities))))
    max_priorty = max(q)[0]
    result = 0
    while q:
        cur = q.popleft()
        if max_priorty == cur[0]:
            max_priorty = max(q)[0]
            result += 1
            if cur[1] == location:
                return result
        else:
            q.append(cur)    
    return -1
print(solution([2, 1, 3, 2], 2))