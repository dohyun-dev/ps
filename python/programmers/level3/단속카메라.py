def solution(routes):
    answer = 0
    check = [False] * len(routes)
    routes.sort(key=lambda x: (x[1], x[0]))
    for i, route in enumerate(routes):
        if check[i]:
            continue
        for j in range(i+1, len(routes)):
            if routes[j][0] <= route[1] <= routes[j][1]:
                check[j] = True
        check[i] = True
        answer += 1
    return answer