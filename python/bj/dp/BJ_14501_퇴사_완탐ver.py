

def dfs(day=0, pay=0):
    global result
    if day >= N:
        if result < pay:
            result = pay
        return

    for i in range(day, N):
        if i + arr[i][0] > N:
            dfs(i + arr[i][0], pay)
        elif i + arr[i][0] <= N:
            check[day] = True
            dfs(i + arr[i][0], pay + arr[i][1])
            check[day] = False


N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
check = [False] * N
result = 0
for i in range(N):
    if i + arr[i][0] > N:
        dfs(i + arr[i][0], 0)
    elif i + arr[i][0] <= N:
        check[i] = True
        dfs(i+arr[i][0], arr[i][1])
        check[i] = False
print(result)