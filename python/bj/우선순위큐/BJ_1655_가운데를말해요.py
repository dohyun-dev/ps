import sys; input = lambda : sys.stdin.readline().rstrip()
from heapq import heappush, heappop

left_q, right_q = [], []
result = []
for i in range(1, int(input())+1):
    num = int(input())

    if len(left_q) == len(right_q):
        heappush(left_q, -num)
    else:
        heappush(right_q, num)
    if left_q and right_q:
        l_num = heappop(left_q)
        r_num = heappop(right_q)
        if -l_num > r_num:
            heappush(right_q, -l_num)
            heappush(left_q, -r_num)
        else:
            heappush(left_q, l_num)
            heappush(right_q, r_num)
    result.append(str(-left_q[0]))
print("\n".join(result))