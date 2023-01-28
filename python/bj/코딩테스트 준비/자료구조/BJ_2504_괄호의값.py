from functools import reduce

data = input()
stack = []
tmp = 1
answer = 0

for i, c in enumerate(data):
    if c == "(":
        stack.append(c)
        tmp *= 2
    elif c == "[":
        stack.append(c)
        tmp *= 3
    elif c == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if data[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if data[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3
print(0 if stack else answer)