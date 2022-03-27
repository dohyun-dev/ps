from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(l, r, c, board):
    q = deque([(l, r, c)])
    board[l][r][c] = 0
    
    while q:
        cur_l, cur_x, cur_y = q.popleft()
        
        # 북 동 남 서 상 하 순으로 순회
        for nl, nx, ny in [(cur_l, cur_x-1, cur_y), (cur_l, cur_x, cur_y+1), (cur_l, cur_x+1, cur_y), (cur_l, cur_x, cur_y-1), (cur_l-1, cur_x, cur_y), (cur_l+1, cur_x, cur_y)]:
            # .이거나 E일때만 board에 dist 초기화 한다
            if 0 <= nl < L and 0 <= nx < R and 0 <= ny < C: 
                if board[nl][nx][ny] == "E":   
                    return f'Escaped in {board[cur_l][cur_x][cur_y] + 1} minute(s).'    # E 일때는 return 
                if board[nl][nx][ny] == ".":
                    board[nl][nx][ny] = board[cur_l][cur_x][cur_y] + 1
                    q.append((nl, nx, ny))
    return 'Trapped!'

result = []

while True:
    L, R, C = map(int, input().split())
    if L == 0:
        break
    
    board = []
    for i in range(L):
        board.append([])
        for r in range(R):
            board[i].append(list(*input().split()))
        input()

    for i in range(L):
        flag = False
        for j in range(R):
            for k in range(C):
                # 시작점을 찾는다
                if board[i][j][k] == "S":
                    flag = True
                    result.append(BFS(i, j, k, board))
            if flag:    break
        if flag:    break
print("\n".join(result))

