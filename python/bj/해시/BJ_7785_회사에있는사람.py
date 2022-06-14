import sys; input = lambda : sys.stdin.readline().rstrip()

N = int(input())
check = set()

for _ in range(N):
    name, order = tuple(input().split())
    if order == "enter":
        check.add(name)
    else:
        check.remove(name)
print("\n".join(sorted(list(check), reverse=True)))