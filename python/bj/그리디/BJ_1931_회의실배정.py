import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
meetings = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
result, cur = 1, meetings[0]

for i in range(1, N):
    if cur[1] <= meetings[i][0]:
        result += 1
        cur = meetings[i]

print(result)

