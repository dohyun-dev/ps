from collections import defaultdict
from itertools import combinations

def binary_search(info_value, query_value):
    left, right = 0, len(info_value) - 1
    last = len(info_value)

    while left <= right:
        mid = (left + right) // 2
        if query_value <= info_value[mid]:
            last = mid
            right = mid - 1
        else:
            left = mid + 1

    if last == -1:
        return 0
    return len(info_value) - last


def solution(info, query):
    info_dict = defaultdict(list)
    for user in info:
        info_key = user.split()
        info_key, info_value = info_key[:-1], int(info_key[-1])


        for i in range(5):
            for c in combinations(info_key, i):
                info_dict["".join(c)].append(info_value)

    for info_value in info_dict.values():
        info_value.sort()

    answer = []
    for q in query:
        q = q.split(" ")
        while "and" in q:
            q.remove("and")
        while "-" in q:
            q.remove("-")
        query_value = int(q[-1])
        search_key = "".join(q[:-1])

        if search_key in info_dict:
            answer.append(binary_search(info_dict[search_key], query_value))
        else:
            answer.append(0)
    return answer

