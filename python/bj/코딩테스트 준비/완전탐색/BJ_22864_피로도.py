A, B, C, M = map(int, input().split())
stamina, answer = 0, 0

for _ in range(24):
    if M < A + stamina:
        stamina = max(stamina - C, 0)
    else:
        stamina, answer = A + stamina, answer + B
print(answer)