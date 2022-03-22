def merge(left, right):
    result = []
    lt, rt = 0, 0
    
    while lt < len(left) and rt < len(right):
        if left[lt] <= right[rt]:
            result.append(left[lt])
            lt += 1
        else:
            result.append(right[rt])
            rt += 1
    
    if lt < len(left):
        result.extend(left[lt:])
    else:
        result.extend(right[rt:])
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left, right = arr[:mid], arr[mid:]
        return merge(merge_sort(left), merge_sort(right))

arr = list(map(int, [*open(0)][1:]))
print(merge_sort(arr))