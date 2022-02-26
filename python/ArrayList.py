import sys; input = lambda : sys.stdin.readline().rstrip()

def check(data):
    stack = []
    for c in data:
        if c in "([":
            stack.append(c)
        elif c == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                return False
        else:
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                return False
    
    if stack:   return False
    return True

def process(data):
    stack = []
    for c in data:
        if c in "([":
            stack.append(c)
        elif c == ")":
            temp = 2
            while stack:
                top = stack.pop()
                if type(top) == int:
                    temp *= top
                elif top == "(":
                    stack.append(temp)
            break
        else:
            temp = 3
            while stack:
                top = stack.pop()
                if type(top) == int:
                    temp *= top
                elif top == "(":
                    stack.append(temp)
            break
    
        temp = 0
        while stack:
            top = stack.pop()
            if type(top) == int:
                temp += top
            else:
                stack.append(top)
        if temp:
            stack.append(temp)
    return stack[-1]

data = input()
if check(data):
    print(process(data))
else:
    print(0)
