stack, answer = [], 0
data = input()
for i, c in enumerate(data):
    if c == "(":
        stack.append(c)
    else:
        if data[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)