from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def ice_search_water(x, y):
    cnt = 0
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            cnt += 1
    return cnt

def search_ice(board):
    temp = []
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                temp.append((i, j))
    return temp

def remove_ice(board, island_list):
    remove_list = []
    temp = []
    for x, y in island_list:
        if board[x][y] != 0:
            cnt = ice_search_water(x, y)
            if cnt != 0:
                remove_list.append((x, y, cnt))
            else:
                temp.append((x, y))
    for x, y, cnt in remove_list:
        board[x][y] = max(0, board[x][y] - cnt)
        if board[x][y] != 0:
            temp.append((x, y))
    return temp

def BFS(x, y, board, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and board[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx, ny))

def search_section(board):
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0 and not visited[i][j]:
                BFS(i, j, board, visited)
                cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0
island_list = search_ice(board)
while True:
    temp = search_section(board)
    if temp >= 2:
        print(answer)
        break
    if len(island_list) == 0:
        print(0)
        break
    island_list = remove_ice(board, island_list)
    answer += 1