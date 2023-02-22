from collections import deque

def fall(level):
    for i in range(7, -1, -1):
        if i < level:
            board[i] = "........"
        else:
            board[i] = board[i-1]

board = [input() for _ in range(8)]

q = deque([(7, 0)])
level = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()

        if board[x][y] == "#":
            continue

        if x == 0 and y == 7:
            print(1)
            exit()

        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1), (x, y), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
            if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] != "#":
                q.append((nx, ny))
    level += 1
    if level < 8:
        fall(level)
print(0)
