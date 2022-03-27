def dfs(cur, computers, visited):
    visited[cur] = True
    for next in computers[cur]:
        if not visited[next] and computers[cur][next] == 1:
            dfs(next, computers, visited)
     

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited)
            answer += 1
    
    return answer

print(solution(3, [[1, 0, 0], [1, 1, 0], [0, 1, 0]]))