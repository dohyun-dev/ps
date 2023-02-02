from heapq import heappush, heappop

min_q, max_q = [], []
check = set()
answer = []

for i in range(int(input())):
    p, l = map(int, input().split())
    heappush(min_q, (l, p, p))
    heappush(max_q, (-l, -p, p))
    check.add(p)

for _ in range(int(input())):
    o = input().split()

    if o[0] == "recommend":
        if o[1] == "1":
            while max_q and max_q[0][2] not in check:
                heappop(max_q)
            answer.append(str(max_q[0][2]))
        else:
            while min_q and min_q[0][2] not in check:
                heappop(min_q)
            answer.append(str(min_q[0][2]))

    elif o[0] == "add":
        p, l = int(o[1]), int(o[2])
        while max_q and max_q[0][2] not in check:
            heappop(max_q)
        while min_q and min_q[0][2] not in check:
            heappop(min_q)
        heappush(min_q, (l, p, p))
        heappush(max_q, (-l, -p, p))
        check.add(p)
    else:
        check.remove(int(o[1]))
print("\n".join(answer))