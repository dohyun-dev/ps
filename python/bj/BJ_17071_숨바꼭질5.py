from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
board = [[-1] * 500001 for _ in range(500001)]
board[N] = 0

q = deque([N, 0])
while q:
    K += 1
    for _ in range(len(q)):
        cur, c = q.popleft()
        for next in [(cur * 2), (cur + 1), (cur - 1)]:
            if 0 <= next <= 500000 and board[c][next] == -1:
                board[c][next] = board[c][cur] + 1
                q.append((next, c + 1))
            if next == K:
                print(board[c][next])
                sys.exit()