from collections import deque
from shutil import move
from tabnanny import check

class Snake:
    dx = [0, 1, 0, -1]    # 동, 남, 서, 북
    dy = [1, 0, -1, 0]
    d = 0
    body = deque()
    
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.body.append((x, y))
        board[x][y] = 1
        
    def change_dir(self, direction):
        if direction == "L":
            if self.d == 0:
                self.d = 3
            else:
                self.d = self.d - 1
        else:
            self.d = (self.d + 1) % 4
    
    def check(self, nx, ny):    # 게임이 끝나는 조건이면 True return        
        if not(0 <= nx < N) or not(0 <= ny < N) or board[nx][ny] == 1:
            return True
        return False
    
    def move(self):
        nx = self.x + self.dx[self.d]
        ny = self.y + self.dy[self.d]
        
        if self.check(nx, ny):   
            return True

        self.x, self.y = nx, ny
        self.body.append((nx, ny))
        
        if board[nx][ny] == 0:
            tx, ty = self.body.popleft()
            board[tx][ty] = 0
        
        board[nx][ny] = 1
        
        
        return False
    

# 0 : 빈공간, 1 : 뱀, 2 : 꼬리
N, K = int(input()), int(input())   # 보드크기 N, 사과의 개수 K
board = [[0] * N for _ in range(N)]
order = deque()
snake = Snake(0, 0)

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

for _ in range(int(input())):
    a, b = input().split()
    order.append((int(a), b))

time = 1
while True:
    if snake.move():
        break
    if order and order[0][0] == time:
        t, d = order.popleft()
        snake.change_dir(d)
    time += 1
print(time)
