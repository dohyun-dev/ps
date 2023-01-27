def calc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    else:
        return a / b

N = int(input())
exp = input()
nums = [int(input()) for _ in range(N)]
stack = []

for c in exp:
    if c.isalpha():
        stack.append(nums[ord(c)-ord("A")])
    else:
        b = stack.pop()
        a = stack.pop()
        stack.append(calc(a, b, c))

print(f'{stack.pop():.2f}')