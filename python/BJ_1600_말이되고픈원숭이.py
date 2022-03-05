from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS():
    q = deque([(0, 0, 0)])
    dist = [[[0] * W for _ in range(H)] for _ in range(K+1)]
    dist[K][0][0] = 0
    
    while q:
        x, y, c = q.popleft()
        
        if x == H-1 and y == W-1:
            return dist[c][x][y]
        if c < K:
            for nx, ny in [(x-2, y-1), (x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2)]:
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and dist[c][nx][ny] == 0:
                    dist[c-1][nx][ny] = dist[c][x][y] + 1
                    q.append((nx, ny, c-1))
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and dist[c][nx][ny] == 0:
                dist[c][nx][ny] = dist[c][x][y] + 1
                q.append((nx, ny, c))
    return -1

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
print(BFS())
