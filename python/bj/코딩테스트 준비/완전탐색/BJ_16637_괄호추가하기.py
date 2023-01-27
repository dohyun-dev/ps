def calc(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    else:
        return a * b


def dfs(idx, result, exp):
    global answer
    if idx == len(operator):
        answer = max(answer, result)
        return
    dfs(idx+1, calc(result, num[idx+1], operator[idx]), f'({exp}{operator[idx]}{num[idx+1]})')

    if idx+2 <= len(operator):
        dfs(idx+2, calc(result, calc(num[idx+1], num[idx+2], operator[idx+1]), operator[idx]), f'({exp}{operator[idx]}({num[idx+1]}{operator[idx+1]}{num[idx+2]}))')

N = int(input())
num, operator = [], []
answer = -2**31

for i in input():
    if i.isdigit():
        num.append(int(i))
    else:
        operator.append(i)

dfs(0, num[0], f"{num[0]}")
print(answer)