import sys; input = lambda : sys.stdin.readline().rstrip()

data, boom = input(), input()
stack = []
while True:
    flag = False
    for c in data:
        stack.append(c)
        if len(stack) >= len(boom) and stack[-1] == boom[-1]:
            temp = []
            for i in range(len(boom)-1, -1, -1):
                temp.append(stack.pop())
                if temp[-1] != boom[i]:
                    while temp:
                        stack.append(temp.pop())
                    break
            else:
                flag = True
    if not flag:
        break
    data = "".join(stack)
    stack.clear()
print(data if data else "FRULA")