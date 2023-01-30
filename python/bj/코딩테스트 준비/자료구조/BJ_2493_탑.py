N, tops = int(input()), map(int, input().split())
stack = []
answer = [0] * (N + 1)

for idx, top in enumerate(tops, 1):
    while stack and stack[-1][0] < top:
        stack.pop()
    if stack:
        answer[idx] = stack[-1][1]
    stack.append((top, idx))

print(" ".join(map(str, answer[1:])))