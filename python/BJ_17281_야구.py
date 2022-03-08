from collections import deque
import sys
from tabnanny import check; input = lambda : sys.stdin.readline().rstrip()

def play(team, n):
    q = deque(team)
    inning, out_cnt = 0, 0
    b1, b2, b3 = 0, 0, 0
    score = 0
    
    while inning < n:
        cur = q.popleft()
        q.append(cur)
        batting = my_team[inning][cur]
        if batting == 0:
            out_cnt += 1
        elif batting == 1:
            score += b3
            b1, b2, b3 = 1, b1, b2
        elif batting == 2:
            score += b2 + b3
            b1, b2, b3 = 0, 1, b1
            for i in range(2):  score += base.popleft()
        elif batting == 3:
            score += b1 + b2 + b3
            b1, b2, b3 = 0, 0, 1
        elif batting == 4:
            score += b1 + b2 + b3 + 1
            b1, b2, b3 = 0, 0, 0
        if out_cnt == 3:
            out_cnt = 0
            inning += 1
            b1, b2, b3 = 0, 0, 0
            continue
        
    return score
        
        

def DFS(l=0):
    global answer
    if l == 9:
        temp = play(team_order, N)
        if answer < temp:
            answer = temp
    else:
        if l == 3:
            DFS(l+1)
        else:
            for i in range(9):
                if not check[i]:
                    check[i] = True
                    team_order[l] = i
                    DFS(l+1)
                    check[i] = False

N = int(input())
my_team = [list(map(int, input().split())) for _ in range(N)]
answer = 0
check, team_order = [False] * 9, [-1] * 9
check[0], team_order[3] = True, 0
DFS()
print(answer)