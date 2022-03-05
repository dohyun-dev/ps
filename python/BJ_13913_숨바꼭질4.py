from collections import deque
import sys

n, k = map(int, input().split())
board = [-1] * 100001
board[n] = 0

q = deque([(n, f'{n}')])

while q:
    cur, result = q.popleft()
    
    if cur == k:
        print(board[cur], result ,sep="\n")
        sys.exit()
    
    for next in [(cur + 1), (cur - 1), (cur * 2)]:
        if 0 <= next <= 100000 and board[next] == -1:
            board[next] = board[cur] + 1
            q.append((next, result + " " + str(next)))