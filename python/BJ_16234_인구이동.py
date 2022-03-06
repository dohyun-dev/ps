from collections import deque
import sys; input = lambda : sys.stdin.readline().rstrip()

def BFS(x, y, visited, board):
    q = deque([(x, y)])
    sum_population = board[x][y]
    visited[x][y] = True
    union_nation = [(x, y)]
    
    while q:
        x, y = q.popleft()
        
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                diff = abs(board[x][y] - board[nx][ny])
                if L <= diff <= R:
                    visited[nx][ny] = True
                    sum_population += board[nx][ny]
                    union_nation.append((nx, ny))
                    q.append((nx, ny))
                    
    if len(union_nation) == 1:
        return 0
    else:
        temp = sum_population // len(union_nation)
        for x, y in union_nation:
            board[x][y] = temp
        return 1

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    
    while True:
        visited, cnt = [[False] * N for _ in range(N)], 0
        answer += 1
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    temp = BFS(i, j, visited, board)   
                    if temp == 0:
                        visited[i][j] = False 
                    cnt += temp
        if cnt == 0:
            break
    print(answer-1)