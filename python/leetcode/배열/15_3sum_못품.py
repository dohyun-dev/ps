import sys; input = lambda : sys.stdin.readline().rstrip()

arr = sorted([-1, 0, 1, 2, -1, -4])
result, temp = [], []
total = 0
for i in range(3):
    temp.append(arr[i])
    total += arr[i]
if total == 0:
    result.append(temp[:])
for i in range(3, len(arr)):
    if total < 0:
        temp.append(arr[i])
        total += arr[i]
    else:
        temp.pop(0)
        total += arr[i]
    if total == 0 and len(temp) == 3:
        result.append(temp[:])
print(result)
        