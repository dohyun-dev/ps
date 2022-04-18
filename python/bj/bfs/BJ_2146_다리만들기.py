from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def min_length_bfs(q, board):
    dist = [[-1] * N for _ in range(N)]
    for x, y in q:
        dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                if board[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    return dist[nx][ny] - 1
    return sys.maxsize

def BFS(x, y, visited, board):
    q = deque([(x, y)])
    island_list = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                island_list.append((nx, ny))
                q.append((nx, ny))
    
    return min_length_bfs(island_list, board)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for i in range(N)]
answer = sys.maxsize;

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and not visited[i][j]:
            answer = min(answer, BFS(i, j, visited, board))
print(answer)