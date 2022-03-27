from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, R = map(int, input().split())
board = [input().split() for _ in range(N)]

q = deque()

for i in range(min(N, M) // 2):
    x, y = i, i
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]: 
        while True:
            nx, ny = dx + x, dy + y
            if i <= nx < N-i and i <= ny < M-i:
                q.append(board[x][y])
                x, y = nx, ny
            else:
                break
        
    q.rotate(-(R % ((N - i * 2) * 2 + (M - i * 2) * 2 - 4)))
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        while True:
            nx, ny = dx + x, dy + y
            if i <= nx < N-i and i <= ny < M-i:
                board[x][y] = q.popleft()
                x, y = nx, ny
            else:
                break

print("\n".join([" ".join(b) for b in board]))