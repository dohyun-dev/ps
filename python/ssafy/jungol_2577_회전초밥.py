import sys; input = lambda : sys.stdin.readline().rstrip(); from collections import defaultdict, deque

n, d, k, c = map(int, input().split())
arr, cache, check = deque([int(input()) for _ in range(n)]), deque(), defaultdict(int)

for i in range(k):
    cache.append(arr[0])
    check[cache[-1]] += 1
    arr.rotate(-1)

answer = len(check) if c in check else len(check) + 1

for _ in range(n):
    remove_ele = cache.popleft()
    cache.append(arr[0])
    check[remove_ele] -= 1
    check[cache[-1]] += 1
    if check[remove_ele] == 0:  
        del check[remove_ele]
    arr.rotate(-1)
    answer = max(answer, len(check) if c in check else len(check) + 1)
    
print(answer)