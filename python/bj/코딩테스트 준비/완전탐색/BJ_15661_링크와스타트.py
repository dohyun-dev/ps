def dfs(l):
    global answer
    if l == N:
        team_a = [i for i in range(N) if visited[i]]
        team_b = [i for i in range(N) if not visited[i]]
        a_score = sum(sum([board[team_a[i]][team_a[j]] + board[team_a[j]][team_a[i]] for j in range(i+1, len(team_a))]) for i in range(len(team_a)))
        b_score = sum(sum([board[team_b[i]][team_b[j]] + board[team_b[j]][team_b[i]] for j in range(i+1, len(team_b))]) for i in range(len(team_b)))
        answer = min(answer, abs(a_score - b_score))
        return

    visited[l] = True
    dfs(l+1)
    visited[l] = False
    dfs(l+1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
answer = float("inf")
dfs(0)
print(answer)
