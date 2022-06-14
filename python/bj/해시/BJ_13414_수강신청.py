import sys; input = lambda : sys.stdin.readline().rstrip()
from collections import defaultdict

K, L = map(int, input().split())
check = {}
result = []

for i in range(L):
    check[input()] = i

for key, value in sorted(check.items(), key=lambda x: x[1]):
    if len(result) == K:
        break
    result.append(key)
print("\n".join(result))