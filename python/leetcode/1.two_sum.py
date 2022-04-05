def solve1():
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j
            
def solve2():
    check = {}
    for idx, num in enumerate(nums):
        check[num] = idx
    
    for idx, num in enumerate(nums):
        if target - num in check:
            return idx, check[target - num]
        
def solve3():
    for i, num in enumerate(nums):
        complement = target - num
        if complement in nums[i+1:]:
            return i, nums[i+1:].index(complement) + i + 1
    
         
nums = [2, 7, 11, 15]
target = 9
print(solve1())
print(solve2())
print(solve3())