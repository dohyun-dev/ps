for t in range(1, int(input())+1):
    N, M = int(input()), int(input())
    graph = [[0] * (N + 1)for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][j] or (graph[i][k] and graph[k][j]):
                    graph[i][j] = 1

    print(f'#{t} {sum([1 if sum([graph[i][j] + graph[j][i] for j in range(1, N+1)]) == N-1 else 0 for i in range(1, N+1)])}')