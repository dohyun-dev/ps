import sys
sys.setrecursionlimit(100000)
def calc(coin, cnt):
    global answer
    if answer < cnt or coin < 0:
        return

    if coin == 0:
        answer = min(answer, cnt)
        return

    if coin % 5 == 0:
        calc(0, coin//5+cnt)
    calc(coin - 2, cnt+1)

N = int(input())
answer = float("inf")
calc(N, 0)
print(answer if answer != float("inf") else -1)