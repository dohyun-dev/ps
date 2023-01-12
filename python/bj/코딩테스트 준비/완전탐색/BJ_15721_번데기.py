A, T, N, cnt = int(input()), int(input()), int(input()), 0
arr1, arr2, arr3 = [0, 1, 0, 1], [0, 0], [1, 1]

while True:
    flag = False
    for i in arr1 + arr2 + arr3:
        if N == i:
            T -= 1
        if T == 0:
            flag = True
            break
        cnt = (cnt + 1) % A
    if flag:
        break
    arr2 += [0]
    arr3 += [1]
print(cnt)