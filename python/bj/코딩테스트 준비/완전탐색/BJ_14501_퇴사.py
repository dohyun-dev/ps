
def DFS(date, profit):
    global answer
    if date > N:
        return
    if date <= N:
        answer = max(answer, profit)

    for i in range(date, N):
        time, benefit = meetings[i]
        DFS(i + time, profit + benefit)


N = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0
DFS(0, 0)
print(answer)