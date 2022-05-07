from heapq import heappush, heappop

def bfs(alp, cop, problems, max_alp, max_cop):
    q = [(0, alp, cop)]
    dist = [[-1] * 500 for _ in range(500)]
    dist[alp][cop] = 0
    
    while q:
        t, a, c = heappop(q)
        if dist[a][c] < t:
            continue
        if a >= max_alp and c >= max_cop:
            return dist[a][c]
        for r_a, r_c, add_a, add_c, time in problems:
            if a < r_a or c < r_c:
                if a < r_a:
                    if dist[r_a][c] > t + r_a - a or dist[r_a][c] == -1:
                        dist[r_a][c] = t + r_a - a
                        heappush(q, (t + r_a - a, r_a, c))
                elif c < r_c:
                    if dist[a][r_c] > t + r_c - c or dist[a][r_c] == -1:
                        dist[a][r_c] = t + r_c - c
                        heappush(q, (t + r_c - c, a, r_c))
            if a >= r_a and c >= r_c:
                na, nc = a + add_a, c + add_c
                if 0 <= na < 500 and 0 <= nc < 500:
                    if dist[na][nc] == -1 or dist[na][nc] > t + time:
                        dist[na][nc] = t + time
                        heappush(q, (t + time, na, nc))       

def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for r_a, r_c, add_a, add_c, time in problems:
        max_alp, max_cop = max(max_alp, r_a), max(max_cop, r_c)
    
    return bfs(alp, cop, problems, max_alp, max_cop)

print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))