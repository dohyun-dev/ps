from heapq import heappush, heappop

def solution(n, works):
    q = []

    for work in works:
        heappush(q, -work)

    while q and n != 0:
        work = -heappop(q)
        if work:
            if work - 1 != 0:
                heappush(q, -work + 1)
            n -= 1
    return sum(w ** 2 for w in q)

print(solution(4, [4, 3, 3]))
