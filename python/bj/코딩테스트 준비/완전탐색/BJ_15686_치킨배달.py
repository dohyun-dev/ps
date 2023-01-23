from itertools import combinations

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
houses = [(i, j) for j in range(N) for i in range(N) if board[i][j] == 1]
shops = [(i, j) for j in range(N) for i in range(N) if board[i][j] == 2]
answer = float("inf")

for combi in combinations(shops, M):
    temp_distance = 0
    for h in houses:
        min_distance = float("inf")
        for c in combi:
            min_distance = min(min_distance, abs(h[0] - c[0]) + abs(h[1] - c[1]))
        temp_distance += min_distance
    answer = min(answer, temp_distance)
print(answer)