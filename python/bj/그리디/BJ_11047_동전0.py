import sys; input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]
result = 0

for coin in coins:
    if K > coin:
        result += K // coin
        K %= coin

print(result)
