
def solution(height:list) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    result = 0

    while left < right:
        if left_max <= right_max:
            if left_max >= height[left]:
                result += left_max - height[left]
            else:
                left_max = height[left]
            left += 1
        else:
            if right_max > height[right]:
                result += right_max - height[right]
            else:
                right_max = height[right]
            right -= 1
    return result

def solution(height):


print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))