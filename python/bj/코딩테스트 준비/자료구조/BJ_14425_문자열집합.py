N, M = map(int, input().split())
arr_set = set(input() for _ in range(N))
print(sum(1 for _ in range(M) if input() in arr_set))