from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(x, y, f_dist, board):
    J_dist = [[-1] * C for _ in range(R)]
    
    J_dist[x][y] = 0
    q = deque([(x,y)])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if not(0 <= nx < R and 0 <= ny < C):
                return J_dist[x][y] + 1
            if J_dist[nx][ny] == -1 and board[nx][ny] != "#":
                if f_dist[nx][ny] == -1 or J_dist[x][y] + 1 < f_dist[nx][ny]: # 상진이가 빨리 도착해야됨 또는 동시에 도착해야됨
                    J_dist[nx][ny] = J_dist[x][y] + 1
                    q.append((nx, ny))
    return "IMPOSSIBLE"

result = []
for _ in range(int(input())):
    C, R = map(int, input().split())
    board = [list(*input().split()) for _ in range(R)]
    F_dist = [[-1] * C for _ in range(R)]
    
    f_q = deque()
    
    # 불과 상진이의 위치를 찾는다.
    for i in range(R):
        for j in range(C):
            if board[i][j] == "*":
                f_q.append((i, j))
                F_dist[i][j] = 0
            elif board[i][j] == "@":
                j_cur = (i, j)
    
    # 불의 dist 갱신
    while f_q:
        x, y = f_q.popleft()
        
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0 <= nx < R and 0 <= ny < C:
                if F_dist[nx][ny] == -1 and board[nx][ny] != "#":
                    F_dist[nx][ny] = F_dist[x][y] + 1
                    f_q.append((nx, ny))
    
    
    result.append(solve(j_cur[0], j_cur[1], F_dist, board))

print("\n".join(map(str, result)))