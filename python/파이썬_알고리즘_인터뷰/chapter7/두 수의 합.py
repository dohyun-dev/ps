def solution(nums, target):
    nums_map = {value: idx for idx, value in enumerate(nums)}

    for idx, num in enumerate(nums):
        if target - num in nums_map and nums_map[target - num] != idx:
            return idx, nums_map[target -  num]

print(solution([2, 7, 11, 15], 9))