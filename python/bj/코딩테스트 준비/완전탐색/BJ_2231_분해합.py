import sys; input = lambda: sys.stdin.readline().rstrip()

num = int(input())
print(([i for i in range(1, num) if sum(map(int, str(i))) + i == num] + [0])[0])