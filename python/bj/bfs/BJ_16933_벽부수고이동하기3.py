from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]
dist = [[[-1] * M for _ in range(N)] for _ in range(K+1)]
dist[0][0][0] = 1

q = deque([(0, 0, 0)])

level = 0
while q:
    for _ in range(len(q)):
        cnt, x, y = q.popleft()
        
        if x == N-1 and y == M-1:
            print(dist[cnt][x][y])
            sys.exit()
        flag = False
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == '1':
                    if level % 2 == 0:  # 낮 일때
                        if cnt + 1 <= K and dist[cnt+1][nx][ny] == -1:
                            dist[cnt+1][nx][ny] = dist[cnt][x][y] + 1
                            q.append((cnt+1, nx, ny))
                    else:   # 밤 일때
                        if not flag:
                            flag = True
                            dist[cnt][x][y] += 1
                            q.append((cnt, x, y))
                else:
                    if dist[cnt][nx][ny] == -1:
                        if flag:
                            dist[cnt][nx][ny] = dist[cnt][x][y]
                        else:
                            dist[cnt][nx][ny] = dist[cnt][x][y] + 1
                        q.append((cnt, nx, ny))
    level += 1
print(-1)