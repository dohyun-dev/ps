import sys
from heapq import heappush, heappop
input = sys.stdin.readline

for t in range(int(input())):
    K, min_q, max_q = int(input()), [], []
    check = [False] * K

    for k in range(K):
        o, num = input().split()

        if o == "I":
            heappush(min_q, (int(num), k, num))
            heappush(max_q, (-int(num), k, num))
            check[k] = True
        else:
            if num == "1":
                while max_q and not check[max_q[0][1]]:
                    heappop(max_q)
                if max_q:
                    check[heappop(max_q)[1]] = False
            else:
                while min_q and not check[min_q[0][1]]:
                    heappop(min_q)
                if min_q:
                    check[heappop(min_q)[1]] = False
        while max_q and not check[max_q[0][1]]:
            heappop(max_q)
        while min_q and not check[min_q[0][1]]:
            heappop(min_q)
    print(f'{max_q[0][2]} {min_q[0][2]}' if min_q and max_q else "EMPTY")