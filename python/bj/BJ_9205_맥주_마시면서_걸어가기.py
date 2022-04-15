from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y):
    q = deque([(x, y, 20)])
    check = set([(x, y)])
    
    while q:
        x, y, beer = q.popleft()
        
        if x == goal_x and y == goal_y:
            return "happy"
        
        for nx, ny in store:
            if (nx, ny) not in check:
                if abs(x -  nx) + abs(y - ny) <= beer * 50:
                    check.add((nx, ny))
                    q.append((nx, ny, 20))
    return "sad"

result = []
for t in range(1, int(input()) + 1):
    n = int(input())
    home_x, home_y = map(int, input().split())
    store = [tuple(map(int, input().split())) for _ in range(n+1)]
    goal_x, goal_y = store[-1]
    result.append(BFS(home_x, home_y))
print("\n".join(result))