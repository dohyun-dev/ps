def search(x, y, student):
    like, empty = 0, 0
    for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]:
        if 0 <= nx < N and 0 <= ny < N:
            if board[nx][ny] == 0:
                empty += 1
            elif board[nx][ny] in student:
                like += 1
    return (like, empty)

def get_score(like):
    return 0 if like == 0 else 10 ** (like-1)

N = int(input())
board = [[0] * N for _ in range(N)]
students = {}

for _ in range(N**2):
    tmp = list(map(int, input().split()))
    students[tmp[0]] = tmp[1:]

for num, student in students.items():
    tmp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                continue
            tmp.append((*search(i, j, student), i, j))
    tmp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    board[tmp[0][2]][tmp[0][3]] = num

print(sum(get_score(search(i, j, students[board[i][j]])[0]) for j in range(N) for i in range(N)))