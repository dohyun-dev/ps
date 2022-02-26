import sys; input = lambda : sys.stdin.readline().rstrip()    

def calc():
    sum1, sum2 = 0, 0
    
    for i in range(N):
        if check[i]:
            for j in range(i+1, N):
                if i != j and check[j]:
                    sum1 += board[i][j]
                    sum1 += board[j][i]
    
    for i in range(N):
        if not check[i]:
            for j in range(i+1, N):
                if not check[j]:
                    sum2 += board[i][j]
                    sum2 += board[j][i]
    
    return abs(sum1 - sum2)
            
def combinations(r, l = 0, start = 0):
    global result
    if l == r:
        result = min(result, calc())
        return
    for i in range(start, N):
        check[i] = True
        combinations(r, l+1, i+1)
        check[i] = False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
check = [False] * N
result = float("inf")
combinations(N // 2)
print(result)