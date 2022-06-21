import sys; input = lambda : sys.stdin.readline().rstrip()

class Shark:
    # 북 남 동 서
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, 1, -1]
    
    def __init__(self, r, c, speed, dir, size, code):
        self.x = r
        self.y = c
        self.speed = speed
        self.dir = dir
        self.size = size
        self.code = code
        
    def move(self):
        nx, ny = self.x, self.y
        
        cnt = self.speed
        while cnt:
            if not(0 < nx + self.dx[self.dir] < R + 1 and 0 < ny + self.dy[self.dir] < C + 1):            
                if self.dir == 0:
                    self.dir = 1
                elif self.dir == 1:
                    self.dir = 0
                elif self.dir == 2:
                    self.dir = 3
                elif self.dir == 3:
                    self.dir = 2
            nx, ny = nx + self.dx[self.dir], ny + self.dy[self.dir]
            cnt -= 1
        
        self.x, self.y = nx, ny
        
        if temp[nx][ny] != 0:
            if temp[nx][ny].size < self.size:
                temp[nx][ny] = self
        else:
            temp[nx][ny] = self
    
    def __str__(self):
        return str(self.code)
            
R, C, M = map(int, input().split())
board = [[0] * (C + 1) for _ in range(R+1)]
answer = 0


if M == 0:
    print(0)
    sys.exit()

for i in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = Shark(r, c, s, d-1, z, i)
    
for i in range(1, C+1):
    for j in range(1, R+1):
        if board[j][i] != 0:
            answer += board[j][i].size
            board[j][i] = 0
            break
    temp = [[0] * (C + 1) for _ in range(R+1)]
    for j in range(1, R+1):
        for k in range(1, C+1):
            if board[j][k] != 0:
                board[j][k].move()
    board = temp
print(answer)
