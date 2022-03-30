from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS():
    q = deque([(0, 0, 0, 0)])
    visited = [[[False] * W for _ in range(H)] for _ in range(31)]
    visited[0][0][0] = False
    
    while q:
        x, y, l, cnt = q.popleft()
        
        if y == H-1 and x == W-1:
            return cnt
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0 and not visited[l][nx][ny]:
                visited[l][nx][ny] = True
                q.append((nx, ny, l, cnt + 1))
        
        if l < K:
            for nx, ny in [(x-2, y-1), (x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2)]:
                if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == 0:
                    if not visited[l-1][nx][ny]:
                        visited[l][nx][ny] = True
                        q.append((nx, ny, l+1, cnt + 1))
        
    return -1

K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
print(BFS())
