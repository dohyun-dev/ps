import sys; input = lambda : sys.stdin.readline().rstrip()

arr = [7,1,5,3,6,4]
answer = 0
min_price = arr[0]
for i in range(1, len(arr)):
    if min_price > arr[i]:
        min_price = arr[i]
    else:
        answer = max(answer, arr[i] - min_price)
print(answer)