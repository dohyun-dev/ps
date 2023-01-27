for _ in range(int(input())):
    stack = []
    for c in input():
        if c == "(":
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")