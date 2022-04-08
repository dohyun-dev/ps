from collections import deque

return_list = [0, set([0, 1, 2, 3]), set([0, 2]), set([1, 3]), set([0, 1]), set([1, 2]), set([2, 3]), set([0, 3])]

def move_list(type):
    return return_list[type]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = []
for t in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    q = deque([(R, C)])
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    cnt, hour = 1, 1
    
    while q:
        if hour == L:
            break
        for _ in range(len(q)):
            x, y = q.popleft()
        
            for i in move_list(board[x][y]):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 0 and not visited[nx][ny]:
                    if (i + 2) % 4 in move_list(board[nx][ny]):
                        visited[nx][ny] = True
                        cnt += 1
                        q.append((nx, ny))
        hour += 1    
    result.append(f'#{t} {cnt}')
print("\n".join(result))