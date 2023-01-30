from itertools import combinations

data = input()
stack, temp = [], []
answer = []

for idx, c in enumerate(data):
    if c == "(":
        stack.append(idx)
    if c == ")":
        if stack:
            temp.append((stack.pop(), idx))
if not stack:
    for i in range(1, len(temp)+1):
        for combi in combinations(temp, i):
            check = [combi[i][j] for j in range(2) for i in range(len(combi))]
            tmp = ""
            for idx, c in enumerate(data):
                if idx not in check:
                    tmp += c
            answer.append(tmp)
    print("\n".join(sorted(list(set(answer)))))