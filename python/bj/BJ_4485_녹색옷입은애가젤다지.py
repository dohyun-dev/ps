import sys; input = lambda : sys.stdin.readline().rstrip()
import heapq

#
# 1 2 3
# 4 5 6
# 7 8 9

# (0, 0):1 (0, 1):2 (0, 2):3
# (1, 0):4 (1, 1):5 (1, 2):6
# (2, 0):7 (2, 1):8 (2, 2):9

def dijkstra(n):
    q = []
    # n * n 2차원 배열 생성 최대값으로 설정
    dist = [[sys.maxsize] * n for i in range(n)]
    
    # 출발지의 cost를 초기화 시켜줌
    dist[0][0] = board[0][0]
    # 우선순위 큐 초기화
    heapq.heappush(q, (dist[0][0], 0, 0))
    
    while q:
        cost, x, y = heapq.heappop(q)
        if dist[x][y] < cost:
            continue
        for nx, ny in [(x-1, y), (x, y+1), (x+1, y), (x, y-1)]: # 북동남서
            if 0 <= nx < n and 0 <= ny < n: # 범위 체크
                next_cost = cost + board[nx][ny]
                # 현재 갱신되어 있는 cost 보다 작으면 dist를 갱신하고 우선순위 큐에 추가
                if next_cost < dist[nx][ny]:    
                    dist[nx][ny] = next_cost
                    heapq.heappush(q, (next_cost, nx, ny))
    return dist[n-1][n-1]
    
    
i = 1
result = []
while(True):
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
            
    result.append(f'Problem {i}: {dijkstra(n)}')
    i += 1
print("\n".join(result))