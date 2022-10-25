from heapq import heappush, heappop

def solution(arguments):
    max_q, min_q = [], []
    for arg in arguments:
        order, num = arg.split()
        num = int(num)
        if order == 'D':
            if num == 1:
                if max_q:
                    heappop(max_q)
                    if not max_q or -max_q[0] < min_q[0]:
                        max_q, min_q = [], []
            else:
                if min_q:
                    heappop(min_q)
                    if not min_q or -max_q[0] < min_q[0]:
                        max_q, min_q = [], []
        else:
            heappush(max_q, -num)
            heappush(min_q, num)
    return [-heappop(max_q), heappop(min_q)] if max_q else [0, 0]



print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))