from collections import deque
from itertools import combinations
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(viruses, board, N, n_cnt):
    q = deque(viruses)
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    
    for x, y in q:
        visited[x][y] = True
        
    while q:
        if n_cnt == 0:
            return cnt
        for _ in range(len(q)):
            x, y = q.popleft()
            
            for nx, ny in [(x-1, y), (x, y + 1), (x+1, y), (x, y-1)]:
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] != "1" and not visited[nx][ny]:
                        if board[nx][ny] == "0":    n_cnt -= 1
                        visited[nx][ny] = True
                        q.append((nx, ny))
        cnt += 1
    return -1

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
viruses = []
answer = sys.maxsize
n_cnt = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == "2":
            viruses.append((i, j))
        elif board[i][j] == "0":
            n_cnt += 1

for v in combinations(viruses, M):
    tmp = BFS(v, board, N, n_cnt)
    if tmp != -1 and answer > tmp:
        answer = tmp
print(answer if answer != sys.maxsize else -1)