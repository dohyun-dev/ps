import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque

class BabyShark:
    size = 2
    cnt = 0
    dx, dy = [-1, 0, 1, 0], [0, 1, 0 ,-1]
    
    def __init__(self, x, y):    
        self.x = x
        self.y = y
        
    def search(self, board, N):
        q = deque([(self.x, self.y)])
        dist = [[0] * N for _ in range(N)]
        dist[self.x][self.y] = 1
        result = []
        while q:
            cur_x, cur_y = q.popleft()
            for i in range(4):
                nx = self.dx[i] + cur_x
                ny = self.dy[i] + cur_y
                if 0 <= nx < N and 0 <= ny < N and dist[nx][ny] == 0 and board[nx][ny] <= self.size:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[cur_x][cur_y] + 1
                    if board[nx][ny] != 0 and board[nx][ny] < self.size:
                        result.append((nx, ny, dist[nx][ny] - 1))
        return sorted(result, key= lambda x : (x[2], x[0], x[1]))

    def eat(self, eat_x, eat_y, board, N):
        self.cnt += 1
        if self.cnt == self.size:
            self.size += 1
            self.cnt = 0
        board[self.x][self.y] = 0
        board[eat_x][eat_y] = 9
        self.x, self.y = eat_x, eat_y
        
    def __str__(self):
        return '아기상어 현재 좌표 : ({}, {}) 크기 : {}'.format(self.x, self.y, self.size)
        

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
time = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            babyshark = BabyShark(i, j)
            break

while True:
    result = deque(babyshark.search(board, N))
    if len(result) == 0:
        break
    eat = result.popleft()
    babyshark.eat(eat[0], eat[1], board, N)
    time += eat[2]
    
print(time)