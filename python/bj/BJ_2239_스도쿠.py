import sys; input = lambda : sys.stdin.readline().rstrip()

section = [set() for _ in range(9)]
row_check = []
col_check = []
zero_list = []

def where_section(x, y):
    if x < 3:
        if y < 3:
            temp = 0
        elif y < 6:
            temp = 1
        else:
            temp = 2
    elif x < 6:
        if y < 3:
            temp = 3
        elif y < 6:
            temp = 4
        else:
            temp = 5
    else:
        if y < 3:
            temp = 6
        elif y < 6:
            temp = 7
        else:
            temp = 8
    return temp

def make_list(x, y):
    ele_list = []
    for i in range(1, 10):
        if str(i) not in row_check[x] and str(i) not in col_check[y] and str(i) not in section[where_section(x, y)]:
            ele_list.append(str(i))
    
    return list(ele_list)

def change_check(x, y, i, t):
    if t == 1:    
        row_check[x].add(i)
        col_check[y].add(i)
        section[where_section(x, y)].add(i)
    else:
        row_check[x].remove(i)
        col_check[y].remove(i)
        section[where_section(x, y)].remove(i)
    
def dfs(board, l=0):
    if l == len(zero_list):
        result = board
        print("\n".join("".join(b) for b in board))
        sys.exit()
        return
    else:
        new_board = [board[i][:] for i in range(9)]
        x, y = zero_list[l]
        for i in make_list(x, y):
            if new_board[x][y] == '0':
                new_board[x][y] = str(i)
                change_check(x, y, str(i), 1)
                dfs(new_board, l+1)
                change_check(x, y, str(i), 2)
                new_board[x][y] = '0'
                
        
board = [list(input()) for _ in range(9)]
zero_list = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            zero_list.append((i, j))
    
# 행
for i in range(9):
    row_check.append(set(num for num in board[i] if num != '0'))

# 컬럼
for i in range(9):
    temp = []
    for j in range(9):
        if board[j][i] != '0':
            temp.append(board[j][i])
    col_check.append(set(temp))

# 섹션
for i in range(9):
    for j in range(9):
        section_idx = where_section(i, j)
        section[section_idx].add(board[i][j])
dfs(board)