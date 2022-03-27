import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

dx = [-2, -2, -1, 1, 2, 2, 1, -1] 
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def BFS(x, y, dist, goal_x, goal_y, l):
    q = deque([(x, y)])
    dist[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        if x == goal_x and y == goal_y:
            return dist[x][y]
        else:
            for i in range(8):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))    
    return 0

T = int(input()) 
result = []
for _ in range(T):
    l = int(input())
    dist = [[-1] * l for _ in range(l)]
    x, y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    result.append(BFS(x, y, dist, goal_x, goal_y, l))

print("\n".join(map(str, result)))
    