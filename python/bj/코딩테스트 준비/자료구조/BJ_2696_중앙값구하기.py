from heapq import heappush, heappop

for t in range(int(input())):
    M, arr = int(input()), []

    for _ in range(M // 10 + 1):
        arr += list(map(int, input().split()))

    answer = []
    for idx in range(1, len(arr) + 1, 2):
        if idx % 2 == 1:
            answer.append(str(sorted(arr[:idx])[idx // 2]))
    print(len(answer))
    if len(answer) < 10:
        print(" ".join(answer))
    else:
        for i in range(len(answer) // 10 + 1):
            print(" ".join(answer[i * 10 : i * 10 + 10]))
