import sys;
from heapq import *

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visitied = set([0])
mst = []
q = [(board[0][i], 0, i) for i in range(N) if board[0][i] != 0]
heapify(q)

while q:
    weight, n1, n2 = heappop(q)
    if n2 not in visitied:
        visitied.add(n2)
        mst.append((weight, n1, n2))
        
        for i in range(N):
            if board[n2][i] != 0 and i not in visitied:
                heappush(q, (board[n2][i], n2, i))

print(visitied)
print(sum([i[0] for i in mst]))
