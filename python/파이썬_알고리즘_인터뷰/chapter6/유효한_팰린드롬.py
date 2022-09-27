import re
from collections import deque

def solution(string):
    sub = re.sub("[^a-zA-Z]", "", string).lower()
    q = deque(sub)
    while q:
        if q.popleft() != q.pop():
            return False
    return True


print(solution("A man, a plan, a canal:"))