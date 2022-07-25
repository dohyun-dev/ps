import sys;

input = lambda: sys.stdin.readline().rstrip()

# 경계를 넘어 설 경우 범위 처리
def range_check(point):
    if point < 0:
        point = N + point % N
    else:
        point = point % N
    if point < 0 or point >= N:
        point = range_check(point)
    return point

def cloud_move(cloud_idx, d, s):
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    # 구름이 d 방향으로 s칸 이동한다
    nx, ny = range_check(clouds[cloud_idx][0] + (dx[d] * s)), range_check(clouds[cloud_idx][1] + (dy[d] * s))

    # 이동한 거 반영
    clouds[cloud_idx] = (nx, ny)


def copy_water(clouds):
    water_cnt = []
    for x, y in clouds:
        cnt = 0
        for nx, ny in [(x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]:
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny]:
                cnt += 1

        water_cnt.append(cnt)

    for cloud, cnt in zip(clouds, water_cnt):
        board[cloud[0]][cloud[1]] += cnt


N, M = map(int, input().split())
board = [[*map(int, input().split())] for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for _ in range(M):
    d, s = map(int, input().split())

    # 구름 이동
    for i in range(len(clouds)):
        cloud_move(i, d, s)

    # 비 내리기
    for x, y in clouds:
        board[x][y] += 1

    # 물 복사
    copy_water(clouds)

    # 구름 사라짐
    temp = []
    for i in range(N):
        for j in range(N):
            if board[i][j] >= 2 and (i, j) not in clouds:
                board[i][j] -= 2
                temp.append((i, j))
    clouds = temp

print(sum(sum(board[i]) for i in range(N)))