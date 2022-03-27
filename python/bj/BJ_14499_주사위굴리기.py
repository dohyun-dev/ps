import sys; input = lambda : sys.stdin.readline().rstrip()

class Dice:
    dx = [0, 0, 0, -1, 1]
    dy = [0, 1, -1, 0, 0]
    
    def __init__(self, x, y):
        self.dice_num = [0] * 7
        self.x = x
        self.y = y
        
    def move(self, dir, board, N, M):
        nx = self.x + self.dx[dir]
        ny = self.y + self.dy[dir]
        if 0 <= nx < N and 0 <= ny < M:    
            if dir == 1:
                self.turn_left()
            elif dir == 2:
                self.turn_right()
            elif dir == 3:
                self.turn_up()
            elif dir == 4:
                self.turn_down()
            
            self.x, self.y = nx, ny
            
            if board[self.x][self.y] == 0:
                board[self.x][self.y] = self.dice_num[6]
            else:
                self.dice_num[6] = board[self.x][self.y]
                board[self.x][self.y] = 0
            
            print(self.dice_num[1])    
                
    def turn_left(self):
        self.dice_num = [0] + [self.dice_num[3], self.dice_num[2], self.dice_num[6], self.dice_num[1], self.dice_num[5], self.dice_num[4]]
    
    def turn_right(self):
        self.dice_num = [0] + [self.dice_num[4], self.dice_num[2], self.dice_num[1], self.dice_num[6], self.dice_num[5], self.dice_num[3]]
        
    def turn_up(self):
        self.dice_num = [0] + [self.dice_num[5], self.dice_num[1], self.dice_num[3], self.dice_num[4], self.dice_num[6], self.dice_num[2]]
        
    def turn_down(self):
        self.dice_num = [0] + [self.dice_num[2], self.dice_num[6], self.dice_num[3], self.dice_num[4], self.dice_num[1], self.dice_num[5]]
    

N, M, x, y, K = map(int, input().split())
dice = Dice(x, y)
board = [list(map(int, input().split())) for _ in range(N)]

for k in list(map(int, input().split())):
    dice.move(k, board, N, M)