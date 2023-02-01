import sys; input = sys.stdin.readline
from collections import defaultdict

trees, cnt = defaultdict(int), 0
while True:
    data = input().rstrip()
    if not data:
        break
    cnt += 1
    trees[data] += 1
for k in sorted(trees.keys()):
    print(f'{k} {trees[k] / cnt * 100:.4f}')