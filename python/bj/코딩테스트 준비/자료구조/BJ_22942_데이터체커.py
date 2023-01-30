N, arr = int(input()), []

for i in range(N):
    x, r = map(int, input().split())
    arr.append((x-r, i, 0))
    arr.append((x+r, i, 1))
arr.sort()

tmp = [x for x, num, status in arr]
if len(tmp) != len(set(tmp)):
    print("NO")
    exit()

stack = []
for x, num, status in arr:
    if not status:
        stack.append((x, num))
    else:
        if stack:
            if stack[-1][1] == num:
                stack.pop()
            else:
                break

if stack:
    print("NO")
else:
    print("YES")

