from collections import deque

def bfs(x, y, section_num):
    q = deque([(x, y)])
    board[x][y] = section_num
    cnt = 1
    while q:
        x, y = q.popleft()
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
            if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == "1":
                board[nx][ny] = section_num
                cnt += 1
                q.append((nx, ny))
    return cnt

def search(x, y):
    tmp = set()
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != "0":
            tmp.add(board[nx][ny])
    return sum(section_cnt[t] for t in tmp) + 1

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
section_cnt = []
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] != "1":
            continue
        section_cnt.append(bfs(i, j, len(section_cnt)))

for i in range(N):
    for j in range(M):
        if board[i][j] == "0":
            answer = max(answer, search(i, j))
print(answer)