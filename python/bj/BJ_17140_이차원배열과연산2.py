import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque

def row_sort():
    global col_size
    max_size = 0
    for i in range(row_size):
        
        counter = defaultdict(int)
        
        for j in range(100):
            if board[i][j] == 0:
                continue
            counter[board[i][j]] += 1
        
        q = deque(sorted(counter.items(), key=lambda x: (x[1], x[0])))
        
        max_size = max(max_size, len(q) * 2)
            
        cnt = 0
        while q:
            if cnt == 100:
                break
            num, num_cnt = q.popleft()
            board[i][cnt], board[i][cnt+1] = num, num_cnt
            cnt += 2
        
        for j in range(cnt, 100):
            if board[i][j] == 0:
                break
            board[i][j] = 0
        print()
    col_size = max_size
            
def col_sort():
    global row_size, board
    board = list(map(list, zip(*board)))
    max_size = 0
    for i in range(100):
        
        counter = defaultdict(int)
        
        for j in range(100):
            if board[i][j] == 0:
                continue
            counter[board[i][j]] += 1
        
        q = deque(sorted(counter.items(), key=lambda x: (x[1], x[0])))
        
        max_size = max(max_size, len(q) * 2)
            
        cnt = 0
        while q:
            if cnt == 100:
                break
            num, num_cnt = q.popleft()
            board[i][cnt], board[i][cnt+1] = num, num_cnt
            cnt += 2
        
        for j in range(cnt, 100):
            if board[i][j] == 0:
                break
            board[i][j] = 0
        print()
    board = list(map(list, zip(*board)))
    row_size = max_size
    
            
def sort_process():
    if board[r-1][c-1] == k:
        return True
    if row_size >= col_size:
        row_sort()
    else:
        col_sort()
    return False
    

r, c, k = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
row_size, col_size = 3, 3
answer = -1

for i in range(3):
    input_arr = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = input_arr[j]

else:
    for i in range(100):
        if sort_process():
            print(i)
            sys.exit()
    print(-1)