from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

F, S, G, U, D = map(int, input().split())
building = [-1] * (F + 1)
building[S] = 0
q = deque([S])

while q:
    cur_floor = q.popleft()
    
    for next_floor in [cur_floor+U, cur_floor-D]:
        if 0 < next_floor <= F and building[next_floor] == -1:
            building[next_floor] = building[cur_floor] + 1
            q.append(next_floor)
print(building[G] if building[G] != -1 else "use the stairs")