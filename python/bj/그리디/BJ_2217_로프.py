import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
ropes = sorted([int(input()) for _ in range(N)], reverse=True)
result = 0
for rope, idx in enumerate(ropes, 1):
    result = max(result, rope * idx)
print(result)