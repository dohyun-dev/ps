import sys; input = lambda : sys.stdin.readline().rstrip()

N, cards1 = int(input()), sorted(list(map(int, input().split())))
M, cards2 = int(input()), list(map(int, input().split()))
result = ["0"] * M

for i in range(M):
    lt, rt = 0, N-1
    while lt <= rt:
        mid = (lt + rt) // 2
        if cards2[i] < cards1[mid]:
            rt = mid - 1
        elif cards2[i] > cards1[mid]:
            lt = mid + 1
        elif cards2[i] == cards1[mid]:
            result[i] = "1"
            break
print(*result)