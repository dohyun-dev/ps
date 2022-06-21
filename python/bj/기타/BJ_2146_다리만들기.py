import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import deque;  sys.setrecursionlimit(10000)

# 섬의 번호를 매기는 함수
def BFS_update_number(x, y, N, board, cnt):
    q = deque([(x,y)])
    board[x][y] = cnt
    
    while q:
        x, y = q.popleft()
        for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= dx < N and 0 <= dy < N and board[dx][dy] == 1:
                board[dx][dy] = cnt
                q.append((dx,dy))
    cnt += 1
    

def BFS(x, y, N, board, map_num):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            if board[x][y] != 0:    # 다른 섬일 때 cnt return(BFS니까 최단거리임)
                return cnt
            for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
                if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and board[dx][dy] != map_num:    # 같은 섬은 check x
                    visited[dx][dy] = True
                    q.append((dx,dy))
        cnt += 1
    return sys.maxsize # return에서 걸리지 않았다는 건 섬이 한 개 밖에 없다는 뜻

def search_edges(x, y, N, board, visited, map_num):
    global result
    if board[x][y] == 0:    # 섬을 벗어나면 DFS가지치기를 하고 다른 섬과의 거리의 최단거리를 구해 result와 비교
        result = min(result, BFS(x, y, N, board, map_num))
        visited[x][y] = False
        return
    for dx, dy in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy]:
                visited[dx][dy] = True
                search_edges(dx, dy, N, board, visited, map_num)
    

if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 1
    
    # 루프를 돌며 각 섬마다 번호를 매긴다(편의상 2부터 매김)
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt += 1
                BFS_update_number(i, j, N, board, cnt)

    visited = [[False] * N for _ in range(N)]
    result = sys.maxsize;
    
    for i in range(N):
        for j in range(N):
            # 각 섬의 영역을 탐색하며 테두리 부분을 찾는다
            if board[i][j] != 0:
                visited[i][j] = True
                search_edges(i, j, N, board, visited, board[i][j])

    print(result if result != sys.maxsize else 0)