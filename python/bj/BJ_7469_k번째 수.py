import sys; input = lambda : sys.stdin.readline().rstrip()

def Q(i, j, k, arr):
    return str(sorted(arr[i-1: j])[k-1])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for _ in range(m):
    i, j, k = map(int, input().split())
    result.append(Q(i, j, k, arr))

print("\n".join(result))