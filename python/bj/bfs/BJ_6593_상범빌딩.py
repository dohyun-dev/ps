from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(l, x, y, board):
    q = deque([(l, x, y)])
    dist = [[[-1] * C for _ in range(R)] for _ in range(L)]
    dist[l][x][y] = 0
    while q:
        l, x, y = q.popleft()
        if board[l][x][y] == 'E':
            return f'Escaped in {dist[l][x][y]} minute(s).'
        for nl, nx, ny in [(l, x-1, y), (l, x, y+1), (l, x+1, y), (l, x, y-1), (l+1, x, y), (l-1, x, y)]:
            if 0 <= nl < L and 0 <= nx < R and 0 <= ny < C and board[nl][nx][ny] != '#' and dist[nl][nx][ny] == -1:
                dist[nl][nx][ny] = dist[l][x][y] + 1
                q.append((nl, nx, ny))         
    return 'Trapped!'       

result = []
while True:
    L, R, C = map(int, input().split())
    if L == 0:  break   # 입력 종료
    board = [[] for _ in range(L)]
    for l in range(L):
        for r in range(R):
            board[l].append(list(input()))
        input()
    
    for i in range(L):
        flag = False
        for j in range(R):
            for k in range(C):
                if board[i][j][k] == 'S':
                    result.append(BFS(i, j, k, board))
                    flag = True
                    break
            if flag:    break
        if flag:    break
print("\n".join(result))