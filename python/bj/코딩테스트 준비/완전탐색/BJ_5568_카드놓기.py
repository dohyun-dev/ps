def combi(l, num=""):
    if l == K:
        answer.add(num)
        return
    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        combi(l+1, num+cards[i])
        check[i] = False

N, K = int(input()), int(input())
cards = [input() for _ in range(N)]
check = [False] * N
answer = set()
combi(0)
print(len(answer))
