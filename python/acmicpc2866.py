from collections import deque

check = [None for _ in range(100001)]   # check 초기화
n, k = map(int, input().split())    # n k 초기화
q = deque([n])                      # 큐 초기화
check[n] = 0                        # 현재 좌표에 0으로

while(q):
    cur = q.popleft()
    
    for next, level in [(cur * 2, 0), (cur + 1, 1), (cur - 1, 1)]:
        if(0 <= next < 100001):
            if check[next] == None:     # 다음 좌표가 방문하지 않았을시 체크next에다가 현재 레벨에서 + 레벨 입력
                check[next] = check[cur] + level
                q.append(next)          # 초기화 됐지만 작을 수 x2의 경우 0초만에 이동하기 때문에 작을경우도 체크해줌
            if check[next] > check[cur] + level:
                check[next] = check[cur] + level
print(check[k]) # 결과 출력