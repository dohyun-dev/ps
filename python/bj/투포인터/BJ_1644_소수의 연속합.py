def primary_arr_factory(n):
    is_primary = [True] * (n + 1)
    is_primary[0], is_primary[1] = False, False

    for i in range(2, n + 1):
        if is_primary[i]:
            for j in range(i + i, n + 1, i):
                is_primary[j] = False

    primary_arr = []
    for i in range(2, n+1):
        if is_primary[i]:
            primary_arr.append(i)
    return primary_arr


N = int(input())
primary_arr = primary_arr_factory(N)
st, end = 0, 1
answer = 0

if primary_arr:
    summary = primary_arr[0]

    while end <= len(primary_arr):
        if summary == N:
            answer += 1
            try:
                summary += primary_arr[end]
            except:
                break
            end += 1
        elif summary > N:
            summary -= primary_arr[st]
            st += 1
        else:
            try:
                summary += primary_arr[end]
            except:
                break
            end += 1
print(answer)

