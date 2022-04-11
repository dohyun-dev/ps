from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def makeNumIsland(x, y, board, visited, num):
    q = deque([(x, y)])
    board[x][y] = num
    visited[x][y] = True
    result = [(x, y, num)]
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] == 1:
                board[nx][ny] = num
                visited[nx][ny] = True
                result.append((nx, ny, num))
                q.append((nx, ny))
    return result

def distEdge(x, y, island_num):
    q = deque()
    result = []
    
    for d in range(4):
        q.append((x + dx[d], y + dy[d], 1, d))  
    
    while q:
        nx, ny, c, d = q.popleft()

        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != island_num:
            if board[nx][ny] == 0:
                nx, ny = nx + dx[d], ny + dy[d]
                q.append((nx, ny, c+1, d))
            else:
                if c > 2:
                    result.append((c-1, board[x][y], board[nx][ny]))
    return result

def distIslandProcess(land):
    edges = []
    for x, y, island_num in land:
        edges += distEdge(x, y, island_num)
    return edges
    
                
def find(node, parent):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a == b:
        return False
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b
    return True
    

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
land = []
visited = [[False] * M for _ in range(N)]
cnt = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and board[i][j] == 1:
            cnt += 1
            land += makeNumIsland(i, j, board, visited, cnt)
            
            
parent = [i for i in range(cnt+1)]
edges = sorted(distIslandProcess(land))
answer = 0

for edge in edges:
    c, a, b = edge 
    
    if union(a, b, parent):
        answer += c        

check = set()
for p in parent[1:]:
    check.add(find(p, parent))

print(answer if len(check) == 1 else -1)