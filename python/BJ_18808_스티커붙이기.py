import sys; input = lambda : sys.stdin.readline().rstrip()

class sticker:
    
    def __init__(self, r, c, board):
        self.r = r
        self.c = c
        self.board = board
    
    def turn(self):
        temp = []
        for i in range(self.c):
            t = []
            for j in range(self.r-1, -1, -1):
                t.append(self.board[j][i])
            temp.append(t)
        self.board = temp
        self.r, self.c = self.c, self.r
        
    def check(self, x, y, n, m, board):
        if x + self.r <= n and y + self.c <= m:
            for i in range(self.r):
                for j in range(self.c):
                    if board[x+i][y+j] == "1" and self.board[i][j] == "1":
                        return False
            return True
        else:
            return False
    
    def update_board(self, x, y, board):
        for i in range(self.r):
            for j in range(self.c):
                if board[x+i][y+j] == "0":
                    board[x+i][y+j] = self.board[i][j] 
    
    def __str__(self):
        return '{} {}\n{}'.format(self.r, self.c, "\n".join(map(str, self.board)))
    
    
# 노트북 세로 가로, 스티커 개수
N, M, K = map(int, input().split())
stickers = []
board = [["0"] * M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    stickers.append(sticker(r, c, [input().split() for _ in range(r)]))
    
for sticker in stickers:
    for turn_cnt in range(4):
        flag = False
        for i in range(N):
            for j in range(M):
                if sticker.check(i, j, N, M, board):
                    sticker.update_board(i, j, board)
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        else:
            sticker.turn()
            
cnt = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == "1":
            cnt += 1
            
print(cnt)     