def suffle(k, end):
    global cards
    for i in range(1, k + 2):
        cnt = 2 ** (k - i + 1)
        cards = cards[end-cnt:end] + cards[:end-cnt] + cards[end:]
        end = cnt

N, result = int(input()), list(map(int, input().split()))

for k1 in range(1, int(N ** 0.5) + 1):
    for k2 in range(1, int(N ** 0.5) + 1):
        cards = list(range(1, N+1))
        suffle(k1, N)
        suffle(k2, N)
        if result == cards:
            print(k1, k2)
            exit()