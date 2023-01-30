priority_dict = {"+": 0, "-": 0, "*": 1, "/": 1, "(": 2}

data = input()
stack = []
answer = ""

for c in data:
    if c.isalpha():
        answer += c
    elif c == ")":
        while stack and stack[-1] != "(":
            answer += stack.pop()
        if stack:
            stack.pop()
    else:
        while stack and stack[-1] != "(" and priority_dict[stack[-1]] >= priority_dict[c]:
            answer += stack.pop()
        stack.append(c)

while stack:
    answer += stack.pop()

print(answer)