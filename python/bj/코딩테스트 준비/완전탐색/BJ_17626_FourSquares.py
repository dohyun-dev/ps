def four_square(n):
    if (n ** 0.5).is_integer():
        return 1
    for i in range(1, int(n ** 0.5) + 1):
        if (int(n - i ** 2) ** 0.5).is_integer():
            return 2
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if (int(n - i ** 2 - j ** 2) ** 0.5).is_integer():
                return 3
    return 4

print(four_square(int(input())))