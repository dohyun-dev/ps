from collections import Counter

arr = [int(input()) for _ in range(3)]
if 60 == arr[0] == arr[1] == arr[2]:
    print("Equilateral")
elif sum(arr) == 180:
    tmp = Counter(arr).most_common()[0][1]
    if tmp == 2:
        print("Isosceles")
    elif tmp == 1:
        print("Scalene")
else:
    print("Error")
