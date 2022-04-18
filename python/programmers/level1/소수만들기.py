from itertools import combinations

def is_primary(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    return len([x for x in combinations(nums, 3) if is_primary(sum(x))])