def solution(people, limit):
    people.sort()
    left, right, cnt = 0, len(people)-1, 0

    while left < right:
        sum_weight = people[left] + people[right]
        if sum_weight <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        cnt += 1
    return cnt + 1 if left == right else cnt

print(solution([70, 50, 80, 50], 100))