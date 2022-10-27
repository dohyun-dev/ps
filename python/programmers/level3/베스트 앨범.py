from collections import defaultdict, Counter


def solution(genres, plays):
    dictionary = defaultdict(list)
    counter = Counter()

    for i in range(len(genres)):
        dictionary[genres[i]].append((i, plays[i]))
        counter[genres[i]] += plays[i]

    result = []

    for k, v in counter.most_common():
        result += list(sorted(dictionary[k], key=lambda x: (-x[1], x[0])))[:2]

    return [r[0] for r in result]


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))