from collections import defaultdict

def solution(input_data:list):
    result = defaultdict(list)

    for data in input_data:
        result["".join(sorted(data))].append(data)

    return result

print(solution(["eat", "tea", "tan", "ate", "nat", "bat"]))