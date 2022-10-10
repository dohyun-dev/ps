def solution(arr:list) -> list:
    result1 = [1] * len(arr)
    result2 = [1] * len(arr)
    for i in range(1, len(arr)):
        result1[i] = result1[i-1] * arr[i-1]
    for i in range(len(arr)-2, -1, -1):
        result2[i] = result2[i+1] * arr[i+1]
    return [a * b for a, b in zip(result1, result2)]

print(solution([1,2,3,4]))
