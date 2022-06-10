import sys; input = lambda : sys.stdin.readline().rstrip()

while (data := input()) != "#":
    count = 0
    for c in data.lower():
        if c in "aeiou":
            count += 1
    print(count)