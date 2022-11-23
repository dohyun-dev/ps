from math import gcd

def gcd_arr(arr):
    answer = arr[0]
    for i in arr:
        answer = gcd(answer, i)
    return answer

def solution(arrayA, arrayB):
    answer = 0
    a_gcd = gcd_arr(arrayA)
    b_gcd = gcd_arr(arrayB)

    if a_gcd != 1 and not any(i % a_gcd == 0 for i in arrayB):
        answer = a_gcd
    if b_gcd != 1 and not any(i % b_gcd == 0 for i in arrayA):
        answer = max(answer, b_gcd)
    return answer