from heapq import heappush, heappop

for t in range(int(input())):
    M, arr = int(input()), []
    min_q, max_q = [], []
    answer = []

    for _ in range(M // 10 + 1):
        arr += list(map(int, input().split()))

    for i, num in enumerate(arr, 1):


        if len(min_q) == len(max_q):
            heappush(min_q, num)
        else:
            heappush(max_q, -num)

        if max_q and min_q and min_q[0] < -max_q[0]:
            max_num = -heappop(max_q)
            min_num = heappop(min_q)
            heappush(max_q, -min_num)
            heappush(min_q, max_num)

        if i % 2:
            answer.append(str(min_q[0]))

    print(len(answer))
    if len(answer) < 10:
        print(" ".join(answer))
    else:
        for i in range(len(answer) // 10 + 1):
            print(" ".join(answer[i * 10 : i * 10 + 10]))
