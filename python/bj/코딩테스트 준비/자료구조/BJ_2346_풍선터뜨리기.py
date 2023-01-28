from collections import deque

N, q = int(input()), deque(enumerate(map(int, input().split()), 1))
answer = []
while q:
    idx, num = q.popleft()
    q.rotate(1-num if num > 0 else -num)
    answer.append(f'{idx}')
print(" ".join(answer))