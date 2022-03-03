# https://www.acmicpc.net/problem/2206

from dis import dis
import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
board = [list(*input().split()) for _ in range(N)]
distance = [[[0] * M for _ in range(N)] for _ in range(2)]
q = deque([(0, 0, 1)])

while q:
    x, y, check = q.popleft()
    if x == N - 1 and y == M - 1:
        print(distance[check][x][y] + 1)
        sys.exit()
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and not(nx == 0 and ny == 0) and distance[check][nx][ny] == 0:
            if board[nx][ny] == "1" and check == 1:  
                distance[0][nx][ny] = distance[1][x][y] + 1
                q.append((nx, ny, 0))
            if board[nx][ny] == "0" and distance[check][nx][ny] == 0:
                distance[check][nx][ny] = distance[check][x][y] + 1
                q.append((nx, ny, check))
print(-1)