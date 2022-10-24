def solution(triangle):
    for i in range(1, len(triangle)):
        for j, value in enumerate(triangle[i]):
            if j == 0:
                triangle[i][j] = triangle[i-1][j] + value
            elif j == i:
                triangle[i][j] = triangle[i-1][j-1] + value
            else:
                triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + value
    return max(triangle[-1])