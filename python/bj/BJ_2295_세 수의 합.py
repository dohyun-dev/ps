import sys; input = lambda : sys.stdin.readline().rstrip()

u = set(int(input()) for _ in range(int(input())))
add_set = set()
for i in u: 
    for j in u: add_set.add(i + j)

answer = 0
for i in u:
    for j in u:
        if (i - j) in add_set:
            answer = max(answer, i)
print(answer)
