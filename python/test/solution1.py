
from collections import deque


comb = []
def connectCheck():
    check = set(comb[0])
    x, y = comb[0]
    q = deque([(x, y)])
    
    while q:
        for nx, ny in [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < H and 0 <= ny < W and not (nx, ny) in check and (nx, ny) in comb:
                check.add((nx, ny))
                q.append((nx, ny))
    
    if len(check) == 4:
        return True
    else:
        return False

def combination(r, c, l=0):
    global answer
    if l == 4:
        answer = max(answer, sum(board[x][y] for x, y in comb))
        return
    else:
        for i in range(r, H):
            if i == r:
                c1 = c
            else:
                c1 = 0
            for j in range(c1, W):
                comb.append((i, j))
                comb(i, j + 1)
                comb.pop()

result = []
for t in range(1, int(input())):
    W, H = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(H)]
    answer = 0
    combination(0, 0)
    result.append(f'#{t} {answer}')
print("\n".join(result))