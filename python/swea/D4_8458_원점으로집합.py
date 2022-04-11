import sys; input = lambda : sys.stdin.readline().rstrip()

result = []
for t in range(1, int(input()) + 1):
    arr = [tuple(map(int, input().split())) for _ in range(int(input()))]
    dist = [abs(x - 0) + abs(y - 0) for x, y in arr]
    if all(map(lambda x: x % 2 == 0, dist)) or all(map(lambda x: x % 2 == 1, dist)):
        answer = 0
        temp = max(dist)
        i = 1
        while True:
            if temp <= 0 and temp % 2 == 0:
                break
            answer += 1
            temp -= i
            i += 1
        result.append(f'#{t} {answer}')
    else:
        result.append(f'#{t} -1')
print("\n".join(result))