import sys; input = lambda : sys.stdin.readline().rstrip()

def dfs(arr, Y=0, S=0):
    global answer
    # Y와 S갯수 증가
    if board[arr[-1][0]][arr[-1][1]] == "Y": Y += 1
    else:   S += 1
    
    # 임도연 파가 3보다 크면 안됨
    if Y > 3:   return
    if Y + S == 7:
        answer.add(str(sorted(arr)))
        return
    for x, y in arr:
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in arr:
                dfs(arr + [(nx, ny)], Y, S)
    
board = [list(input()) for _ in range(5)]
answer = set()
for i in range(5):
    for j in range(5):
        dfs([(i, j)])
print(len(answer))