def solution(nums):
    get_size = len(nums) // 2
    nums = set(nums)
    return get_size if len(nums) >= get_size else len(nums)