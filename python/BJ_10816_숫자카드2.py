from bisect import bisect_left, bisect_right

N, cards = int(input()), sorted(list(map(int, input().split())))
M, targets = int(input()), list(map(int, input().split()))
print(" ".join([str(bisect_right(cards, target) - bisect_left(cards, target)) for target in targets]))