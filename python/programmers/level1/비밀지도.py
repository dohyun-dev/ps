def invert_binary(num, n):
    binary_num = ""
    while num > 0:
        binary_num = str(num % 2) + binary_num
        num //= 2
    return '0' * (n - len(binary_num)) + binary_num

def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        a = invert_binary(a, n)
        b = invert_binary(b, n)
        temp = ""
        for i in range(n):
            if a[i] == "1" or b[i] == "1":
                temp += "#"
            else:
                temp += " "
        answer.append(temp)
    return answer