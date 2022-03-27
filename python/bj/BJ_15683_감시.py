import sys; input = lambda : sys.stdin.readline().rstrip()
from copy import deepcopy

class Camera:
    directions = {
        1: [[(-1, 0)], [(0, 1)], [(1, 0)], [(0, -1)]],
        2: [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
        3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
    }    
    
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.direction = 0
        
    def shooting(self, board, N, M):
        for dir in self.directions[self.type][self.direction]:        
            dx, dy = dir
            cnt = 1
            while True:
                nx, ny = self.x + (dx * cnt), self.y + (dy * cnt)
                if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 6:    
                    if board[nx][ny] == 0:
                        board[nx][ny] = "#"
                else:   break
                cnt += 1
                
    def __str__(self):
        return str(self.type) + " " + "(" + str(self.x) + ", " + str(self.y) + ")"
    
def count_board(board):
    return sum(sum([1 for i in b if i == 0]) for b in board)
                
def DFS(l, cameras, board):
    global min_blind_spot
    if l == len(cameras):
        temp = deepcopy(board)
        for camera in cameras:
            camera.shooting(temp, N, M)
        # print("\n" + "\n".join(map(str, temp)))
        min_blind_spot = min(count_board(temp), min_blind_spot)
    else:
        if cameras[l].type == 5:
            DFS(l+1, cameras, board)
        elif cameras[l].type == 2:
            for i in range(2):
                cameras[l].direction = i
                DFS(l+1, cameras, board)
        else:
            for i in range(4):
                cameras[l].direction = i
                DFS(l+1, cameras, board)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cameras = []

for i in range(N):
    for j in range(M):
        if board[i][j] != "#" and 0 < board[i][j] < 6:
            cameras.append(Camera(board[i][j], i, j))

cameras.sort(key= lambda x: -x.type)            
min_blind_spot = N * M
DFS(0, cameras, board)
print(min_blind_spot)