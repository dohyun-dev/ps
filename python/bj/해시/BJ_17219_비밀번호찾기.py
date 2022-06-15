import sys; input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
password_dict = {}

for _ in range(N):
    a, b = tuple(input().split())
    password_dict[a] = b

print("\n".join(password_dict[input()] for _ in range(M)))