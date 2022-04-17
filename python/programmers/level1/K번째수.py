def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

from collections import defaultdict
d = defaultdict(int)
print(d.keys())