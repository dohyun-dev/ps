from itertools import permutations

wish_word, N = input(), int(input())
books = [input().split() for _ in range(N)]
answer = []

for p in permutations(books):
    check, total = wish_word, 0
    for book in p:
        price, name, flag = int(book[0]), book[1], False
        for i in name:
            if i in check:
                check = check.replace(i, " ", 1)
                flag = True
        if flag:
            total += price

        if not check:
            break
    if total != 0:
        answer.append(total)

print(min(answer) if answer else -1)