def solution(land):
    answer = [[0] * 4 for i in range(len(land))]
    for i in range(4):
        answer[0][i] = land[0][i]
    for i in range(1, len(land)):
        for j in range(4):
            answer[i][j] = land[i][j] + max(answer[i-1][:j] + answer[i-1][j+1:])
    return max(answer[len(land)-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))