from collections import deque


def board_proces(board, visited):
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0 and visited[i][j]:
                board[i][j] -= 1

def BFS(x, y):
    q = deque([(x, y, 1)])
    visited = [[False] * c for _ in range(r)]
    visited[x][y] = True
    liveCnt = [0] * 1250001
    
    while q:
        x, y, l = q.popleft()
        
        liveCnt[l] += 1
        liveCnt[l + board[x][y]] -= 1
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny, l+1))
    
    now_cnt = 0
    max_cnt = -1
    max_day = -1
    for day in range(1, 1250001):
        now_cnt += liveCnt[day]
        if max_cnt < now_cnt:
            max_cnt = now_cnt
            max_day = day
    return max_day, max_cnt    
        
    
    

for t in range(1, int(input()) + 1):
    r, c = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(r)]
    x, y = map(int, input().split())
    a, b = BFS(x, y)
    print(f'#{t} {a}일 {b}개')