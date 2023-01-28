N = int(input())
stack, num = [], 1
result = []

for _ in range(N):
    target = int(input())

    while num <= target:
        stack.append(num)
        result.append("+")
        num += 1

    if stack.pop() == target:
        result.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(result))