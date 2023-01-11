import sys; input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = float('inf')
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if abs(M - answer) > abs(M - sum) and M >= sum:
                answer = sum
print(answer)