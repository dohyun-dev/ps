import sys; input = lambda : sys.stdin.readline().rstrip()

class Block:
    type1 = [1, 1, 1, 1]
    type2 = [[1, 1], [1, 1]]
    type3 = [[1, 0], [1, 0], [1, 1]]
    type4 = [[1, 0], [1, 1], [0, 1]]
    type5 = [[1, 1, 1], [0, 1, 1]]
    
    def __init__(self, type):
        if type == 1:
            self.shape = self.type1
        elif type == 2:
            self.shape = self.type2
        elif type == 3:
            self.shape = self.type3
        elif type == 4:
            self.shape = self.type4
        else:
            self.shape = self.type5
            
    def turn(dir):
    
    def 
            

N, M = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]

