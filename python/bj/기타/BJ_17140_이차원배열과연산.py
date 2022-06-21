import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict, deque

def row_sort():
    global col_size
    max_size = 0
    for i in range(row_size):
        
        counter = defaultdict(int)
        
        # 나오는 숫자의 갯수를 센다
        for j in range(100):
            if board[i][j] == 0:
                continue
            counter[board[i][j]] += 1
        
        # 정렬수행
        q = deque(sorted(counter.items(), key=lambda x: (x[1], x[0])))
        
        # max값 갱신
        max_size = max(max_size, len(q) * 2)
        
        
        # q에 하나의 인덱스에 2개의 원소가 들어가있어서 2씩증가
        cnt = 0
        while q:
            if cnt == 100:
                break
            num, num_cnt = q.popleft()
            board[i][cnt], board[i][cnt+1] = num, num_cnt
            cnt += 2
        
        # 나머지 남은 공간을 0으로 채워줌
        for j in range(cnt, col_size):
            board[i][j] = 0
    # 현재 col_size 갱신
    col_size = max_size
            
def col_sort():
    global row_size
    max_size = 0
    for i in range(col_size):
        counter = defaultdict(int)
        
        for j in range(100):
            if board[j][i] == 0:
                continue
            counter[board[j][i]] += 1
        
        q = deque(sorted(counter.items(), key=lambda x: (x[1], x[0])))
        
        max_size = max(max_size, len(q) * 2)
        
        cnt = 0
        while q:
            if cnt == 100:
                break
            num, num_cnt = q.popleft()
            board[cnt][i], board[cnt+1][i] = num, num_cnt
            cnt += 2
        
        for j in range(cnt, row_size):
            board[j][i] = 0
    row_size = max_size
            
def sort_process():
    # 정답의 조건과 같다면 True 반환
    if board[r-1][c-1] == k:
        return True
    # 첫번째 조건대로 row_size가 col_size보다 크다면 R 연산 수행
    if row_size >= col_size:
        row_sort()
    # 두번째 조건대로 col_sisze가 row_size보다 크다면 C 연산 수행
    else:
        col_sort()
    return False
    

r, c, k = map(int, input().split())
# 최대 크기가 100이니까 100 x 100 배열 생성
board = [[0] * 100 for _ in range(100)]
row_size, col_size = 3, 3
answer = -1

for i in range(3):
    input_arr = list(map(int, input().split()))
    for j in range(3):
        board[i][j] = input_arr[j]


for i in range(101):
    if sort_process():
        print(i)
        sys.exit()
print(-1)