from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def bfs(x, y, board):
    q = deque([(x, y)])
    board[x][y] = 0
    
    while q:
        x, y = q.popleft()
        if x == g_x and y == g_y:
            return str(board[x][y])
        for nx, ny in [(x-2, y+1), (x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1), (x+1, y-2), (x-1, y-2), (x-2, y-1)]:
            if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))  
result = []
for _ in range(int(input())):
    l = int(input())
    board = [[-1] * l for _ in range(l)]
    s_x, s_y = map(int, input().split())
    g_x, g_y = map(int, input().split())
    result.append(bfs(s_x, s_y, board))
print("\n".join(result))