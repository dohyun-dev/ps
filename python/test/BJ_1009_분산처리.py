for _ in range(int(input())):
    a, b = map(int, input().split())
    print((a ** b - 1) % 10 + 1)